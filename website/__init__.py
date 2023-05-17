from flask import Flask

def create_app():
    app = Flask(__name__) # name of file being run
    app.config['SECRET_KEY'] = 'secretkey' # this reason should be given how it works
    
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app # this returns the app when called