import json, traceback, jsonschema, time, requests
from flask_login import current_user, login_required
from flask import current_app, jsonify, redirect, request, Blueprint, url_for
from web.models import db, Payment, Course, Enrollment
from web.apis.make_slug import generate_random_id
from web.apis.errors import handle_response

from os import getenv, path
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

pay = Blueprint('pay', __name__)

@pay.route('/init-payment/<string:course_slug>', methods=['POST', 'GET'])
@login_required
def init_payment(course_slug):
    try:
        # Retrieve course information from the database
        #course = Course.query.get(course_id)
        course = Course.query.filter(Course.slug == course_slug).first()
        if not course:
            return handle_response(message="Course Not Found", alert='alert-danger'), 404

        # Prepare payment payload
        payload = {
            "tx_ref": f"-tx-techa-{generate_random_id(k=5)}",
            "amount": course.fee or 100,
            "currency": "USD",
            "redirect_url": f"{request.url_root}payment-callback",
            "customer": {
                "email": current_user.email if current_user.is_authenticated else request.args.get('email', 'hello@intellect.com'),
                "phonenumber": current_user.phone if current_user.is_authenticated and current_user.phone else None,
                "name": current_user.name or current_user.username if current_user.is_authenticated else None
            },
            "payment_options": "card, ussd, banktransfer, credit, mobilemoneyghana",
            "customizations": {
                "title": f"{course.title} . Russian Developers Program",
                "logo": url_for('static', filename='img/favicon/favicon.png', _external=True)
            }
        }

        # Make a POST request to get the payment link
        headers = {
            "Authorization": f"Bearer {getenv('RAVE_SECRET_KEY')}",
            "Content-Type": "application/json"
        }

        response = requests.post("https://api.flutterwave.com/v3/payments", json=payload, headers=headers)
        response_data = response.json() if response else { }
        payment_link = response_data.get("data", {}).get("link")

        if not payment_link:
            return handle_response(message="Failed to retrieve payment link", alert='alert-danger')

        # Save transaction details to the database
        payment_data = {
            'currency': payload['currency'],
            'tx_amount': payload['amount'],
            'tx_ref': payload['tx_ref'],
            'tx_status': 'pending',
            'provider': 'FlutterWave',
            'tx_id': None,
            'user_id': current_user.id,
            'course_id': course.id
        }
        new_payment = Payment(**payment_data)
        db.session.add(new_payment)
        db.session.commit()

        # Redirect the user to the payment link
        return redirect(payment_link)

    except Exception as e:
        traceback.print_exc()
        return handle_response(message=str(e), alert='alert-danger'), 500

@pay.route('/payment-callback', methods=['GET'])
@login_required
def payment_callback():
    try:
        # Extract data from query parameters
        status = request.args.get('status')
        transaction_id = request.args.get('transaction_id')
        tx_ref = request.args.get('tx_ref')

        # Check if the transaction was successful and meets my criteria
        payment = Payment.query.filter(Payment.tx_ref == tx_ref ).first()

        if status == 'successful':
            # Proceed with processing the successful payment
            # -------------------------------------------
            # Make a request to verify the transaction
            headers={"Authorization": f"Bearer {getenv('RAVE_SECRET_KEY')}"}

            verify_by_txref_endpoint = f"https://api.flutterwave.com/v3/transactions/{tx_ref}"
            verify_by_txid_endpoint = f"https://api.flutterwave.com/v3/transactions/{transaction_id}/verify"

            response = requests.get(verify_by_txid_endpoint, headers=headers)
            
            # Check if the request was successful
            if response.status_code == 200:
                # Convert the JSON string to a Python dictionary
                response_data = response.json() if response else {}

                # Check if transaction data exists in the response
                if 'data' in response_data:
                    transaction_data = response_data['data']
                    if (
                        transaction_data['status'] == "successful"
                        and transaction_data['amount'] >= payment.tx_amount
                        and transaction_data['currency'] == payment.currency
                    ):
                        # Success! Confirm the customer's payment
                        payment.tx_status = transaction_data['status']
                        payment.tx_id =  transaction_data['id']

                        # Create enrollment record for the user and the course
                        enrollment = Enrollment(
                            user=current_user, user_id=current_user.id, 
                            course=payment.course, course_id=payment.course.id
                            )
                        db.session.add(enrollment)

                        db.session.commit()
                        #return jsonify({'message': 'Transaction verified successfully', 'data': transaction_data}), 200
                        return redirect(url_for('main.learn', slug=payment.course.slug))
                    else:
                        # Inform the customer their payment was unsuccessful
                        return jsonify({'message': 'Transaction Verification Failed', 'data': transaction_data}), 400
                else:
                    return jsonify({'message': 'No transaction data found'}), 400
            else:
                return jsonify({'message': 'Failed to verify transaction'}), 400

        if status == 'cancelled':
            # Success! Confirm the customer's payment
            payment.tx_status = status
            #payment.tx_id =  transaction_data['id'] ->No Transact
            db.session.commit()
            #return jsonify({'message': 'Transaction verified successfully', 'data': transaction_data}), 200
            return redirect(url_for('main.prev', slug=payment.course.slug))

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@pay.route('/check-pending-txn', methods=['GET'])
def check_pending():
    try:
        # Your existing logic for checking transaction status
        pending_payments = Payment.query.filter(Payment.tx_status == 'pending').all()
        print([x for x in pending_payments], '\n')
        for payment in pending_payments:
            # Process pending payments
            # Make a request to verify the transaction using tx_ref
            headers={"Authorization": f"Bearer {getenv('RAVE_SECRET_KEY')}"}
            verify_by_txref_endpoint = f"https://api.flutterwave.com/v3/transactions/{payment.tx_ref}"
            response = requests.get(verify_by_txref_endpoint, headers=headers)
            
            if response.status_code == 200:

                response_data = response.json()

                if response_data.get('status') == 'successful':
                    # Update payment status and create enrollment
                    payment.tx_status = response_data.get('status')
                    payment.tx_id = response_data.get('id')
        
                    enrollment = Enrollment(
                        user=payment.user, user_id=payment.user.id, 
                        course=payment.course, course_id=payment.course.id
                    )
                    db.session.add(enrollment)
                    return "('Pending TXNS Updated')"
            else:
                current_app.logger.error('Failed to verify transaction')
                return "Error: Failed to verify transaction"

        db.session.commit()
        
    except Exception as e:
        # Handle exceptions
        print(type(response))
        return f"Error:-> {(e) }"

