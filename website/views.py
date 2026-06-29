from flask import Blueprint,render_template,request,redirect,url_for
from flask_login import current_user,login_required
from .model import Note
from . import db

views =Blueprint("views",__name__)

@views.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('views.user'))
    return render_template("home.html")

@views.route('/userpage',methods=['GET','POST'])
@login_required
def user():
    if request.method=='POST':
        data=request.form.get('action-trigger')
        note=Note(data=data,user_id=current_user.id)
        db.session.add(note)
        db.session.commit()
    return render_template("userpage.html",user=current_user)