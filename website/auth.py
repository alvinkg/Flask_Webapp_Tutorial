from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required,logout_user, current_user
# setup file as Blueprint
auth = Blueprint('auth', __name__)

@auth.route("/login/", methods=["GET", "POST"])
def login():
    # return "<p>Login</p>"
    if request.method == "POST":
        # get info from form
        email = request.form.get('email')
        password = request.form.get('password1')
        
        # query db table User for email
        user = User.query.filter_by(email=email).first()
        if user:
            # hash password and compare with the hashed password in User
            if check_password_hash(user.password, password):
                flash('Logged in successfully.', category='success')
                login_user(user, remember=True) # store inside flask server browser  login history
                return redirect(url_for('views.home'))
            else:
                flash('incorrect password. ', category='error')
        else:
                flash('Email does not exist.', category='error')
            
            
    return render_template("login.html")

@auth.route("/logout/")
@login_required
def logout():
    # bring them back to the login view
    logout_user()
    return redirect(url_for('auth.login'))
    # return "<p>Logout</p>"
    # return render_template(".html")

@auth.route("/signup/", methods=["GET", "POST"])
def signup():
    # return "<p>Sign Up</p>"
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        confirmPassword = request.form.get('confirmPassword')
        
        user = User.query.filter_by(email=email).first()
        if user:
         flash('Email exists.', category='error')   
        if len(email) < 4:
            flash('Email must be longer than three characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than one character.', category ='error')
        elif password1 != confirmPassword:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password must be longer than six characters.', category='error')
        else:
            # add user to dB
            new_user = User(email=email, first_name=first_name, password=password1) #generate_password_hash(password1, method='sha256')
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)            
            flash('Accounted created.', category='success')
            return redirect(url_for('views.home'))
            
    return render_template("signup.html")