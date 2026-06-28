from flask import Blueprint,render_template,request,flash,redirect,url_for
from .model import User,Note
from . import db
from werkzeug.security import generate_password_hash,check_password_hash

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
            else:
                flash('Password incorrect!',category='error1')
        else:
            flash('Incorrect email.try again!..',category='error1')
    return render_template("login.html",boolean=True)

@auth.route('/logout')
def logout():
    return "<h1>LOGOUT<h1>"

@auth.route('/signin',methods=['GET','POST'])
def signin():
    data=request.form
    print(data)
    if request.method=='POST':
        Name=request.form.get('name')
        Email=request.form.get('username')
        password=request.form.get('password')
        password2=request.form.get('confirm_password')

        user=User.query.filter_by(email=Email).first()

        if user:
            flash('Email already exists!',category='error')
        elif len(Email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
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
    
            flash('Account created!', category='success')

            return redirect(url_for('views.home'))
            
        
    return render_template("signin.html")