from flask import Flask, url_for, render_template, request, redirect, session
from dbcmds import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    if session.get('logged_in'):
        return render_template('home.html')
    else:
        return render_template('index.html', message="Hello!")


@app.route('/donor/', methods=['GET'])
def donor():
    if session.get('logged_in'):
        return render_template('home.html')
    else:
        return render_template('donor.html', message="Hello!")


@app.route('/request/', methods=['GET'])
def request():
    if session.get('logged_in'):
        return render_template('home.html')
    else:
        return render_template('request.html', message="Hello!")


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            username=request.form['username']
            password=request.form['password']
            email=request.form['email']

            addUser(username ,email, password)
            return redirect(url_for('login'))
        except:
            return render_template('index.html', message="User Already Exists")
    else:
        return render_template('login.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        u = request.form['username']
        p = request.form['password']
        
        if getPassword(u) == p:
            session['logged_in'] = True
            return redirect(url_for('index'))
        return render_template('index.html', message="Incorrect Details")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))

if(__name__ == '__main__'):
    app.secret_key = "ThisIsNotASecret:p"
    app.run(debug=True)