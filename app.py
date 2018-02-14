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
            session['logged'] = True #Mark the user as "logged in"
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
        if (pwd == "") or (pwd != rpwd):
            return render_template('register.html')
        if userr in users:
            return render_template('register.html')
        else:
            users[userr] = pwd
            #return redirect(url_for('/'), code=302)
            return render_template("login.html")
            #check_user()

@node.route('/logout', methods=['POST'])
def logout():
    session['logged'] = False
    return render_template('login.html')

"""These upcoming functions don't have any practical use at the moment,
   but may be useful in the near future"""


@node.route('/hub', methods=['POST'])
def home():
    if request.method == "POST":
        """nothing to do here yet, more to come soon"""


@node.route('/my-account', methods=['POST'])
def account():
    return render_template('my-account.html')
    """nothing to do here yet, more to come soon"""


@node.route('/popular-videos', methods=['POST'])
def popular():
    return render_template('popular-videos.html')
    """nothing to do here yet, more to come soon"""


@node.route('/my-videos', methods=['POST'])
def own_videos():
    return render_template('my-videos.html')
    """nothing to do here yet, more to come soon"""


@node.route('/search', methods=['POST'])
def search():
    search_string = request.form['search']
    return render_template('search.html', search_string=search_string)


if __name__ == "__main__":
	node.secret_key = os.urandom(15)
	node.run(debug = True)

