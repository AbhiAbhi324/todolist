from flask import Blueprint,render_template,request,flash
from .model import User,Note
from . import db

auth =Blueprint("auth",__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    data=request.form
    print(data)
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
        
        if len(Email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(Name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
     
            new_user = User(email=Email, password=password, name=Name)
            db.session.add(new_user)
            db.session.commit()
    
            flash('Account created!', category='success')
            
        
    return render_template("signin.html")