
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
#from flask_bootstrap import Bootstrap
from flask_moment import Moment
from slugify import slugify
from web.utils import time_ago, user_role, entry
from flask_socketio import SocketIO
from nltk.tokenize import sent_tokenize
db = SQLAlchemy()
bcrypt = Bcrypt()
s_manager = LoginManager()
s_manager.login_view = 'auth.signin'
s_manager.login_message_category = 'info'
mail = Mail()
migrate = Migrate()
#bootstrap = Bootstrap()
moment = Moment()
socketio = SocketIO()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile(entry + "/confiq.py")

    db.init_app(app)
    bcrypt.init_app(app)
    s_manager.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    #bootstrap.init_app(app)
    moment.init_app(app)
    socketio.init_app(app, manage_session=False)
    from web.auth.routes import auth
    from web.main.routes import main
    from web.editor.routes import editor
    from web.chatme.routes import chat
    from web.pays.routes import pay
    from web.errors.handlers import errors
    from web.socketio.route import socket_bp
    
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(editor)
    app.register_blueprint(chat)
    app.register_blueprint(pay)
    app.register_blueprint(errors)
    app.register_blueprint(socket_bp)

    #My-New APi Endpoints
    from web.apis.x_courses.x_categories import x_category_bp
    app.register_blueprint(x_category_bp)

    from web.apis.x_courses.x_course import x_course_bp
    app.register_blueprint(x_course_bp)

    from web.apis.x_courses.x_lesson import x_lesson_bp
    app.register_blueprint(x_lesson_bp)

    from web.apis.x_courses.x_topic import x_topic_bp
    app.register_blueprint(x_topic_bp)

    #For Recommendations | But Could Not Install `surprise` just yet
    from web.x_recommend.routes import x_recommend_bp
    app.register_blueprint(x_recommend_bp)

    app.jinja_env.filters['time_ago'] = time_ago.timeAgo
    app.jinja_env.filters['type'] = user_role.type
    app.jinja_env.filters['sent_tokenize'] = sent_tokenize
    app.jinja_env.filters['slugify'] = slugify
    
    with app.app_context():
        db.create_all()
    return app
