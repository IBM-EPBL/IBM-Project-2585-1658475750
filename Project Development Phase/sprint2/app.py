from dbcmds import *
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    login=0
    if session.get('logged_in'):
        login=1
        return render_template('home.html',login_var=login)
    else:
        return render_template('index.html', message="Hello!",login_var=login)


@app.route('/donor/', methods=['GET','POST'])
def donor():
    login=1
    print(request.method)
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
            return render_template('index.html', message="User Already Exists",login_var=login)
        except:
            return render_template('index.html', message="User Already Exists",login_var=login)
    else:
        if session.get('logged_in'):
            login=1
            return render_template('donor.html',login_var=login)
        else:
            login=0
            return render_template('login.html', message="Hello!" ,login_var=login)


@app.route('/request/', methods=['GET'])
def requests():
    login=0
    if session.get('logged_in'):
        login=1
        return render_template('request.html',login_var=login)
    else:
        return render_template('login.html', message="Hello!",login_var=login)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    login=0
    if request.method == 'POST':
        try:
            username=request.form['username']
            password=request.form['password']
            email=request.form['email']

            addUser(username ,email, password)
            return redirect(url_for('login'))
        except:
            return render_template('index.html', message="User Already Exists",login_var=login)
    else:
        return render_template('login.html',login_var=login)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    login=0
    if request.method == 'GET':
        return render_template('login.html',login_var=login)
    else:
        u = request.form['username']
        p = request.form['password']
        ps = getPassword(u)
        
        if ps == "User Does not exist":
            return redirect(url_for('index'), message="User Does not exist",login_var=login)

        elif ps == p:
            login=1
            session['logged_in'] = True
            return redirect(url_for('index')
            )
        return render_template('index.html', message="Incorrect Details",login_var=login)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    login=0
    return render_template('index.html',login_var=login)

if(__name__ == '__main__'):
    app.secret_key = "ThisIsNotASecret:p"
    app.run(debug=True)