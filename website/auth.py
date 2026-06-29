from flask import Blueprint,render_template,request,flash,redirect,url_for
from .model import User
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
import re
from flask_login import login_user,login_required,logout_user,current_user

auth =Blueprint("auth",__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')

        user=User.query.filter_by(email=username).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Successfull Login',category='success1')
                login_user(user,remember=True)
                return redirect(url_for('views.user'))
                
            else:
                flash('Password incorrect!',category='error1')
        else:
            flash('Incorrect email.try again!..',category='error1')
    return render_template("login.html",user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route('/signin',methods=['GET','POST'])
def signin():
    if request.method=='POST':
        Name=request.form.get('name')
        Email=request.form.get('username')
        password=request.form.get('password')
        password2=request.form.get('confirm_password')

        user=User.query.filter_by(email=Email).first()
        email_pattern=r'^[a-z0-9\.-]+@gmail\.com$'

        if user:
            flash('Email already exists!',category='error')
        elif not re.match(email_pattern, Email):
            flash('Enter valid email only!',category='error')
        elif len(Name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
     
            new_user = User(email=Email, password=generate_password_hash(password), name=Name)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
    
            flash('Account created!', category='success')

            return redirect(url_for('views.user'))
            
        
    return render_template("signin.html",user=current_user)