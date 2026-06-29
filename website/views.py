from flask import Blueprint,render_template
from flask_login import current_user,login_required

views =Blueprint("views",__name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/userpage')
@login_required
def user():
    return render_template("userpage.html")