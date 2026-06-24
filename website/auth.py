from flask import Blueprint

auth =Blueprint("auth",__name__)

@auth.route('/login')
def login():
    return "<h1>LOGIN</h1>"

@auth.route('/logout')
def logout():
    return "<h1>LOGOUT<h1>"

@auth.route('/signin')
def signin():
    return "<h1>SIGN IN<h1>"