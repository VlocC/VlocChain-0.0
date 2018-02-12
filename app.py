"""
VlocChain
Authors: Owen Sullivan, Joe DeGrand, Carter Nesbitt
Filename: app.py
"""

from flask import Flask
from flask import request, session, render_template, redirect, flash
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
vlocchain.append(create_genesis())
users = {} #full user dictionary, usernames

"""
When this place gets pinged, make a new user and send the information
out so the pinger can recieve it
"""


@node.route('/', methods=['GET', 'POST'])
def index():
	if not session.get('logged'):
		return render_template('login.html')
	else:
		return render_template('hub.html')


@node.route('/login', methods=['POST'])
def check_user():
    username = request.form.get("username")
    pword = request.form.get("password")
    conf_pword = request.form.get("confirm_password")
    if (pword == conf_pword):
        users[username] = pword
    if request.method == "POST":
        usern = request.form['username']
        pwd = request.form['password']
        if usern in users:
            session['logged'] = True
        else:
            # return "YEET"
            flash("Wrong password!")
            session['logged'] = False
        return index()



@node.route('/sendvideo', methods=['GET'])
def sendvids():
	return render_template('sendvideo.html')



@node.route('/send', methods=['POST', 'GET'])
def player():
	if request.method == "POST":
		usernew = request.form['username']
		video = request.form['video']
		print(video)
		if usernew in users:
			#socket
			return "It Worked!"
		else:
			render_template("sendvideo.html")



@node.route('/register', methods=['POST', 'GET'])
def render():
	return render_template('register.html')



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
			return "Success"



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
    return render_template('search.html')


if __name__ == "__main__":
	node.secret_key = os.urandom(15)
	node.run(debug = True)


