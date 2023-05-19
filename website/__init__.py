from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# instance of a new db app
db = SQLAlchemy()
# give a name
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) # name of file being run
    app.config['SECRET_KEY'] = 'secretkey' # this reason should be given how it works
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    # register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    # import models
    from .models import User, Note

    with app.app_context():
        db.create_all()       
        
    login_manager = LoginManager()
    login_manager.login_view ='auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app # this returns the app when called
    
    # create_database(app)
# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app=app)
#         print('Database created')