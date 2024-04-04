from flask import current_app, jsonify, render_template, Blueprint, url_for
from flask_login import current_user, login_required

#from flask_mailman import EmailMessage
from flask_mail import Message
from slugify import slugify
from sqlalchemy import desc

from web.models import Course
from web.api import course , tutor , user 

#import socket
#socket.getaddrinfo('localhost', 25)

from web import mail

tests = Blueprint('tests', __name__)

#courses -> landing ->
#@tests.route("/")
@tests.route('/welcome')
def welcome():
    return render_template("welcome/welcome.html", data = course.courses)

@tests.route("/")
@login_required
def usr():
   # page = request.args.get('page', 1, type=int)
    #posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('indexx.html', rater = course.rater, progress = user.progress, 
                           badger = user.badger, badge = user.badge, time = user.time, recomend=user.recomend)

@tests.route('/explore')
def explore():
    course = Course.query.all()
    return render_template("courses/explore.html", course=course, data = course.courses)

@tests.route('/prev2/<string:slug>')
@tests.route('/course2/<string:slug>')
def prev(slug):
    course = Course.query.filter_by(slug=slug).first_or_404()
    return render_template('courses/prev.html', rview = course.rev_test, course = course, data = course.one)

@tests.route("/us")
def us():
    return render_template('welcome/us.html', title='About Us')

@tests.route("/blog")
def blog():
    return render_template('blog.html', title='Read')

@tests.route('/school')
@login_required
def school():
    return render_template("school.html")

@tests.route('/test/<string:cid>')
def details_test(cid):
    c = Course.query.filter_by(id=cid).first_or_404()
    return render_template('courses/cos.html', c = c)

#quiz
@tests.route('/quiz')
@login_required
def quiz():
    return render_template("quiz/quiz.html")
    
@tests.route('/qdetail', defaults={'one':'one'})
@tests.route('/qdetail/<string:one>', defaults={'one':'one'})
@login_required
def qdetails(one):
    return render_template("quiz/qdetail.html")

@tests.route('/qresult')
@login_required
def qresult():
    return render_template("quiz/qresult.html")


#path
@tests.route('/paths')
@login_required
def path():
    return render_template("path/path.html")

@tests.route('/path', defaults={'one':'one'})
@tests.route('/path-of/<string:one>', defaults={'one':'one'})
@login_required
def path_of(one):
    return render_template("path/path-of.html")


#instructors
@tests.route('/tutors')
@login_required
def tutor_list():
    #p = request.args.get('p', 1, type=int)
   # t = User.query.order_by(User.id.desc()).paginate(p=p, pp=12)
    #t = User.query.filter(User.role == 1,).order_by(User.id.desc()).paginate(page=p, per_page=12)
    return render_template("instructor/tutors.html", tutors = 't')

   # page = request.args.get('page', 1, type=int)
    #posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)

@tests.route('/tutor', defaults={'t':'t'})
@tests.route('/tutor/<string:t>', defaults={'t':'t'})
@login_required
def tut(t):
    return render_template("instructor/tutor.html", tutor = tutor.info )

@tests.route('/play')
@login_required
def player():
    return render_template("misc/play.html")

@tests.route('/materi')
@login_required
def materi():
    return render_template("misc/material.html")

@tests.route('/syllabus')
@login_required
def syllabus():
    return render_template("misc/syllabus.html")

@tests.route('/../json/search.json')
@tests.route('/json/search.json')
def search():
    #return render_template("static/json/search.json")
    #return url_for('static/json/search.json')
    #return redirect(url_for('static', filename='json/search.json'))
    #s = Course.query.all()
    #s = jsonify(s)
    #find = Course.query.order_by(desc(Course.created))
   # find = Course.query()
    #return jsonify([{'name': n.name, 'data': n.get_data(), 'timestamp': n.timestamp } for n in notifications])
    c = Course.query.all()
   #return jsonify([{ 'label': c.title, 'url': c.slug } for c in c])
    return jsonify([{ 'label': c.title, 'url': url_for('main.prev', slug=c.slug) } for c in c])

"""
    return [
    {
        "label": "settings",
        "url": f"/{current_user.username}/update" if current_user.is_authenticated else url_for('auth.signin')
    },
    {
        "label": "Dashboards > Elearning",
        "url": "/"
    },
    {
        "label": "Dashboards > School",
        "url": "/school"
    },
    {
        "label": "Data Science",
        "url": "/data"
    },
    {
        "label": "Internet Of Things",
        "url": "/iot"
    },
    {
        "label": "Web Programming",
        "url": "/programming"
    },
    {
        "label": "Artificial Intelligence",
        "url": "/course/<slug>"
    },
    {
        "label": "Computer Networking",
        "url": "/courses/<slug>"
    },
    {
        "label": "Python Programming",
        "url": "/course/<slug>"
    },

]
"""


#pip install awesome-slugify
@tests.route('/slugged')
def slug_it():
    str = 'gdg uut -/ hd_ yyey'
    return slugify('one koz_hdhue eee'+ str)

#socket.getaddrinfo('localhost', 5003)

@tests.route('/flaskmail')
def sendmail():
    print(current_app.config['MAIL_PASSWORD'])
    msg = Message('Hello', sender ='jameschristo962@gmail.com',
        recipients = ['jameschristo962@gmail.com'] )
    msg.body = 'Hello Flask message sent from Flask-Mail'
    mail.send(msg)
    return 'Sent'

"""
@tests.route('/flaskmailman')
def flaskmail():

    subject, from_email, to = 'hello', 'from@example.com', 'jameschristo962@gmail.com'
    #subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'
    html_content = '<p>This is an <strong>important</strong> message.</p>'

    msg = EmailMessage(subject, html_content, from_email, [to])
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    return 'Sent'

"""