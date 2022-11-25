from dbcmds import *
from flask import Flask, redirect, render_template, request, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    login=session.get('logged_in')
    if session.get('logged_in'):
        return render_template('home.html',login_var=login)
    else:
        return render_template('index.html', message="Hello!",login_var=login)

@app.route('/donor/', methods=['GET','POST'])
def donor():
    if not session.get('logged_in'):
        return redirect(url_for('index'))

    if request.method == 'POST':
        try:
            name=request.form['name']
            age=request.form['age']
            email=request.form['email']
            bloodgrp=request.form['bloodgrp']
            mobno=request.form['mobno']
            inputAddress=request.form['inputAddress']
            inputCity=request.form['inputCity']
            inputState=request.form['inputState']
            inputZip=request.form['inputZip']
            gender=request.form['gender']
            insertDonor(name , age , email , bloodgrp, mobno , gender , inputAddress , inputCity , inputState , inputZip)
            return render_template('home.html', message="Details Registered")
        except:
            return render_template('home.html', message="Some error while registering please try again")
    else:
        return render_template('donor.html')


@app.route('/request/', methods=['GET', 'POST'])
def requests():
    if not session.get('logged_in'):
        return redirect(url_for('index'))

    if request.method == 'POST':
        try:
            
            name=request.form['name']
            age=request.form['age']
            email=request.form['email']
            bloodgrp=request.form['bloodgrp']
            mobno=request.form['mobno']
            inputAddress=request.form['inputAddress']
            inputCity=request.form['inputCity']
            inputState=request.form['inputState']
            inputZip=request.form['inputZip']
            gender=request.form['gender']
            process_request(name , age , email , bloodgrp, mobno , gender , inputAddress , inputCity , inputState , inputZip)
            return render_template('home.html', message="Request posted successfully")
        except:
            return render_template('home.html', message="Request is not processed please try again")
    else:
        return render_template('request.html')        


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            username=request.form['username']
            password=request.form['password']
            # password=generate_password_hash(password)
            # print(check_password_hash(password ,"Manoj007!"))
            email=request.form['email']

            if addUser(username ,email, password) == "Username Exists":
                return render_template('login.html', message="User Already Exists")
                
            return redirect(url_for('login'))
        except:
            return render_template('login.html', message="User Already Exists")
    else:
        return render_template('login.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        session['logged_in'] = False
        return render_template('login.html')
    else:
        u = request.form['username']
        p = request.form['password']
        ps = getPassword(u)
        print(ps , p)
        print( check_password_hash(ps,p) )
        if ps == "User Does not exist":
            return redirect(url_for('index'))

        elif ps == p:
            session['logged_in'] = True
            return redirect(url_for('index'))
        
        return render_template('login.html' , message="wrong password")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))

if(__name__ == '__main__'):
    print(os.getenv("PL"))
    app.secret_key = "ThisIsNotASecret:p"
    app.run( "0.0.0.0" , debug=True)
    