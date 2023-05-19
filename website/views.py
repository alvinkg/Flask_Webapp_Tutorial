from flask import Blueprint, render_template
from flask_login import login_user, login_required,logout_user, current_user

# setup file as Blueprint
views = Blueprint('views', __name__)

# this is where we store out routes

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

