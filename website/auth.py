from flask import Blueprint, render_template, request, flash

# setup file as Blueprint
auth = Blueprint('auth', __name__)

@auth.route("/login/", methods=["GET", "POST"])
def login():
    # return "<p>Login</p>"

    return render_template("login.html")

@auth.route("/logout/")
def logout():
    return "<p>Logout</p>"
    # return render_template(".html")

@auth.route("/signup/", methods=["GET", "POST"])
def signup():
    # return "<p>Sign Up</p>"
    if request.method == "POST":
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        confirmPassword = request.form.get('confirmPassword')
        
        if len(email) < 4:
            flash('Email must be longer than three characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than one character.', category ='error')
        elif password1 != confirmPassword:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password must be longer than six characters.', category='error')
        else:
            # add user to dB
            flash('Accounted created.', category='success')
    return render_template("signup.html")