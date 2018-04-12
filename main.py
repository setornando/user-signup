from flask import Flask, request, redirect, render_template
import cgi
import os
import re

app = Flask(__name__)
app.config['DEBUG']= True

app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    password_confirmation = request.form['password_confirmation']
    email = request.form['email']

    username_error = ''
    password_error = '' 
    confirmation_error = ''
    email_error = ''
    if username == "":
        username_error = "Please enter a valid username."
    elif len(username) < 3 or len(username) > 20:
        username_error = "Please enter a username between 3 and 20 characters."
        
    elif " " in username:
        username_error = "Username cannot contain spaces."
        
    
    if password == "":
        password_error = "Please enter a valid password."
    elif len(password) < 3 or len(password) > 20:
        password_error = "Please enter a password between 3 and 20 characters."
        password = ""
    elif " " in password:
        password_error = "Password cannot contain spaces."
        password = ""
    
    if password_confirmation == "" or password_confirmation != password:
        confirmation_error = "Passwords do not match."
        password_confirmation = ""
    
    if email != "":

        if len(email) < 3 or len(email) > 20:
            email_error="The email address must be between 3 and 30 characters long."    
        elif not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-Z0-9-.]+$)",email):
            email_error= "The email address must have a single @, a single ., and contain no spaces."
    
    if not username_error and not password_error and not confirmation_error and not email_error:
        return render_template('welcome_page.html', username = username)
    else:
        return render_template('index.html', username = username, 
        username_error = username_error, 
        password_error = password_error, 
        confirmation_error = confirmation_error,
        email = email, 
        email_error = email_error)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome_page.html', username=username)

if __name__ == "__main__":
    app.run()
