from flask import Blueprint,render_template,request,flash

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
        
        if password!=password2:
            flash('password doesnt matches',category='error')
        else:
            flash('sucessfully created',category='success')
            
        
    return render_template("signin.html")