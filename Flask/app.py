#Step – 1(import necessary library)
from flask import Flask
from flask import Flask, render_template, request, redirect, session
from hashlib import sha512
import os
#Step – 2 (configuring your application)
app = Flask(__name__)
app.secret_key = 'Varun-Myneni'     #you can set any secret key but remember it should be secret
#step – 3 (creating a dictionary to store information about users)
user = {"username": "admin", "password": "admin" }
user1 = {"username": "varun", "password": "varun"}
@app.route('/')
def index():
    return '<!DOCTYPE html><html><head><title>Index Page</title></head><body><br><br><br><br><br><br><h1 align="center">This is Index Page</h1><h4 align="center"><a href="/login" >Login-Page</a></h4><h4 align="center"><a href="/dashboard">DashBoard-Page</a></h4></body></html>'
#Step – 4 (creating route for login)
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')     
        if ((username == user['username'] and password == user['password']) or (username == user1['username'] and password == user1['password'])):
            print('Regular Validation Successful')
            c = user['username']+user['password']
            uhash = sha512(c .encode()).hexdigest()
            wc = username+password
            whash = sha512(wc .encode()).hexdigest()
            if(whash==uhash):
                session['user'] = username
                return redirect('/auth')
            else:
                return redirect('/auth404')
        return '<h4 align="right"><a href="/">Index</a></h4><h1 align="center">Wrong username or password</h1>'    #if the username or password does not matches 
    return render_template("app.html")

@app.route('/auth')
def auth():
    return '<!DOCTYPE html><html><head><title>Successfull Auth</title></head><body><br><br><br><br><h1 align="center"><b><font color="green">User Authentication Successful</font></b><h1><h2 align="center"><b>Authentication Done with SHA-512</b></h2><br><br><br><h1 align="center"><b>Redirecting..</b></h1><br><p align="center">you should be redirected automatically to target URL:<a href="/dashboard">/dashboard</a>. if not click the link</p></body></html>'

@app.route('/auth404')
def auth404():
    return '<!DOCTYPE html><html><head><title>Un-Successfull Auth</title></head><body><br><br><br><br><h1 align="center"><b><font color="red">!!User Authentication UN-Successful!!</font></b><h1><h2 align="center"><b>Authentication Done with SHA-512</b></h2><br><br><br><h1 align="center"><b>Redirecting..</b></h1><p align="center">you should be redirected automatically to target URL:<a href="/login">/login</a>. if not click the link</p></body></html>'

#Step -5(creating route for dashboard and logout)
@app.route('/dashboard')
def dashboard():
    if('user' in session and session['user'] == user['username']):
        return '<!DOCTYPE html><html><head><title>DashBoard Page</title></head><body><h5 align="right"><a href="/">Index-Page</a></h5><h5 align="right"><a href="/logout">Log-Out</a></h5><br><h1 align="center">Welcome to the dashboard</h1></body></html>'
    #here we are checking whether the user is logged in or not
    return '<!DOCTYPE html><html><head><title>DashBoard Page</title></head><body><h5 align="right"><a href="/">Index-Page</a></h5><h1 align="center">You are not logged in.</h1></body></html>'  #if the user is not in the session
#Step -6(creating route for logging out)
@app.route('/logout')
def logout():
    session.pop('user')         #session.pop('user') help to remove the session from the browser
    return redirect('/')
#Step -7(run the app)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
