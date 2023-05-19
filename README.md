# Flask Webapp Tutorial

Tutorial using Flask to build a website with authentication and a database. To do this we will install flask-login and flask-sqlalchemy modules.

We create an python package 'website' using the __init__.py allowing us to import what methods we need, like 'create_app'.

## templating

This is a base template that is used to replicate other files for web pages by overriding them.
We override the base template base.html using jinja code.  We use {{ }} allowing pythonic code to be written as well {% %} as blocks for templating using inheritance.
We can do blocks, if and for loops, or pass variables.

## blueprinting

We build blueprints for our auth and login.

## bootstrap

## static files

These include images, javascript files to format pages.

## Bugs

```bash
<button type="button" class="close" data-bs-dismiss="alert">
    <span aria-hidden="true">
        &times;
    </span>
</button>
```

Flask_SQLAlchemy no longer accepts an app argument to 'create_all'.  So we need to write the code so:

```bash
    # register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    # import models
    from .models import User, Note

    with app.app_context():
        db.create_all()
    
    return app # this returns the app when called
```