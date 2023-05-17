from flask import Blueprint, render_template

# setup file as Blueprint
views = Blueprint('views', __name__)

# this is where we store out routes

@views.route('/')
def home():
    return render_template("home.html")

