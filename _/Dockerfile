# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR .

# Copy the current directory contents into the container at /.
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Define environment variable for MySQL connection
ENV MYSQL_HOST=localhost \
    MYSQL_USER='root' \
    MYSQL_PASSWORD='' \
    MYSQL_DB='russiant'

# Run the app using Gunicorn (replace "app" with your Flask app object)
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:web"]
