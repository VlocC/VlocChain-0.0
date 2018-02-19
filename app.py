"""
VlocChain
Authors: Owen Sullivan, Joe DeGrand, Carter Nesbitt
Filename: app.py
"""

from flask import Flask
from flask import request, session, render_template, redirect, flash, url_for
from lxml import html
import json
import requests
import hashlib as hasher
import datetime as date
import random
import user_class
import os
node = Flask(__name__)


"""
All global variables
"""
nodes = [] #All known nodes get added here
vlocchain = [] #the main chain, most updated
exchanges = [] #all the exchanges
miner_address = "yeet" #temporary
users = {} #full user dictionary, usernames
users["admin"] = "pass" 
#weblink = "https://127.0.0.1:5000/" #The main webwage of the website

"""
When this place gets pinged, make a new user and send the information
out so the pinger can recieve it
"""


"""
The home page of the website. If the user isn't logged in yet, it will bring them to the login page. Otherwise, the hub page will be rendered.
"""
@node.route('/', methods=['GET', 'POST'])
def index():
	if not session.get('logged'): #If the user is not logged in
		return render_template('login.html')
	else: #If the user is logged in
		return render_template('hub.html')


"""
The form from "login.html", sent when the user clicks the "submit" button
"""
@node.route('/login', methods=['POST'])
def check_user():
    if request.method == "POST":
        usern = request.form['username']
        pwd = request.form['password']
        if usern in users: #If the user exists
            if (users[usern] == pwd):
                session['logged'] = True #Mark the user as "logged in"
                session['username'] = usern
        else:
            flash("Wrong password!")
            session['logged'] = False #Marks the user as "not logged in"
        return index() #Reloads the page with 'logged' marked as either "True" or "False"



"""
The webpage where videos can be exchanged between users
"""
@node.route('/sendvideo', methods=['GET'])
def sendvids():
	return render_template('sendvideo.html') #Renders the send video page



@node.route('/send', methods=['POST', 'GET'])
def player():
	if request.method == "POST":
		usernew = request.form['username'] #Gets the username part of the form
		video = request.form['video'] #Gets the password part of the form
		print(video)
		if usernew in users:
			#socket
			return "It Worked!"
		else:
			render_template("sendvideo.html")



"""
The place where a new user can be created
"""
@node.route('/register', methods=['POST', 'GET'])
def render():
	return render_template('register.html')



"""
The form on the "register.html" page, that sends what the user typed in for username, password, and confirm password. If the username is already taken, or their passwords don't match, it will just refresh the page. Otherwise, their information will be added to the the dictionary "users".
"""
@node.route('/sendregister', methods=['POST', 'GET'])
def send_register():
    if request.method == "POST":
        userr = request.form['username']
        pwd = request.form['password']
        rpwd = request.form['confirm_password']
        mail_address = request.form['email']
        if (pwd == "") or (pwd != rpwd) or (mail_address == ""):
            return render_template('register.html')
        if userr in users:
            return render_template('register.html')
        else:
            users[userr] = pwd
            #return redirect(url_for('/'), code=302)
            return render_template("login.html")
            #check_user()

"""Returns user to login page after logging out of an account"""
@node.route('/logout', methods=['POST'])
def logout():
    session['logged'] = False
    session['username'] = None
    return render_template('login.html')


"""Home page for a user"""
@node.route('/hub', methods=['POST'])
def home():
    """nothing"""

"""Page for account settings and status"""
@node.route('/my-account', methods=['POST'])
def account():
    return render_template('my-account.html')

@node.route('/change-password', methods=['GET'])
def change_password():
    return render_template('change-password.html')


"""Form that checks the credentials to change the password of an existing user"""
@node.route('/send-new-pass', methods=['GET', 'POST'])
def send_new_pass():
    user_conf = request.form.get('conf_user')
    password_conf = request.form.get('conf_pass')
    new_password = request.form.get('new_pass')
    confirm_new = request.form.get('conf_new_pass')
    if user_conf in users:
        if users[user_conf] == password_conf: #makes sure password is correct
            if new_password == confirm_new: #confirms new password
                users[user_conf] = new_password #changes password
                session['logged'] = False
                session['username'] = None
                return render_template('login.html')
    #if anything is not correct, bring user back to change password page
    return render_template('change-password.html')

"""Page that displays popular videos of entire site"""
@node.route('/popular-videos', methods=['POST'])
def popular():
    return render_template('popular-videos.html')


"""Page that displays videos created/owned by signed in user"""
@node.route('/my-videos', methods=['POST'])
def own_videos():
    return render_template('my-videos.html')


"""Page that shows results for search bar"""
@node.route('/search', methods=['POST'])
def search():
    search_string = request.form['search']
    return render_template('search.html', search_string=search_string)

"""Form that deletes a given account"""
@node.route('/delete-account', methods=['GET'])
def delete_account():
    del_user = session['username']
    session['logged'] = False
    del users[session['username']] ## remove user from user list
    session['username'] = None
    return render_template('login.html')

if __name__ == "__main__":
	node.secret_key = os.urandom(15)
	node.run(debug = True)

