"""
VlocChain
Authors: Owen Sullivan, Joe DeGrand, Carter Nesbitt
Filename: app.py
"""

from flask import Flask
from flaskext.mysql import MySQL
from flask import request, session, render_template, redirect, flash, url_for
from lxml import html
from werkzeug.utils import secure_filename
from video_class import Video
import json
import requests
import hashlib as hasher
import datetime as date
import random
import user_class
import os
import operator
import configdb
node = Flask(__name__)
node = configdb.opendb(node)
mysql = MySQL(node)

UPLOAD_FOLDER = "./newVideos"
ALLOWED_EXTENSIONS = set(["mp4", "avi", "webm"])
node.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

"""
All global variables
"""
nodes = [] #All known nodes get added here
vlocchain = [] #the main chain, most updated
exchanges = [] #all the exchanges
videos = [] ## holds all instances of video class
miner_address = "yeet" #temporary
users = {} #full user dictionary, usernames
admin = user_class.User("admin", "", "")
users[admin] = "pass"  
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
        session['logged'] = False
        usern = request.form['username']
        pwd = request.form['password']
        for user in users:
            if user.username == usern: #If the user exists
                if (users[user] == pwd):
                    session['logged'] = True #Mark the user as "logged in"
                    session['username'] = user.username
            else:
                session['logged'] = False #Marks the user as "not logged in"
        return redirect("/") #Reloads the index page with 'logged' marked as either "True" or "False"


"""
The webpage where videos can be exchanged between users
"""
@node.route('/sendvideo', methods=['GET'])
def sendvids():
	return render_template('sendvideo.html') #Renders the send video page

@node.route('/send', methods=['POST', 'GET'])
def player():
        if request.method == "POST":
                video = request.files["video"]
                filename = video.filename
                if ('.' in filename): ## makes sure filename is recognizable
                    if (filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS): ## if correct file
                        filename = secure_filename(filename) ## allows os.path.join to recognize name
                        video.save(os.path.join(node.config['UPLOAD_FOLDER'], filename))
                        return render_template("hub.html") ## worked, send back to hub
                return render_template("sendvideo.html") ## didn't work, reload page

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
            return redirect("register")
        if userr in users:
            return render_template('register.html')
        else:
            new_user = user_class.User(userr, "", mail_address)
            users[new_user] = pwd
            return redirect("/")

"""Returns user to login page after logging out of an account"""
@node.route('/logout', methods=['POST'])
def logout():
    session['logged'] = False
    session['username'] = None
    return redirect("/")

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
    for user in users:
        if user.username == user_conf:
            if users[user] == password_conf: #makes sure password is correct
                if new_password == confirm_new: #confirms new password
                    users[user] = new_password #changes password
                    session['logged'] = False
                    session['username'] = None
                    return render_template('login.html')
    #if anything is not correct, bring user back to change password page
    return render_template('change-password.html')

"""Page that displays popular videos of entire site"""
@node.route('/popular-videos', methods=['POST'])
def popular():
    video_views = {}
    sorted_videos = []
    for video in videos:
        video_views[video] = video.views
    sorted_videos = sorted(video_views.items(), reverse=True, key=operator.itemgetter(1))
    return render_template('popular-videos.html', videos = sorted_videos)


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
    del_usern = session['username']
    session['logged'] = False
    for user in users:
        if user.username == del_usern:
            del users[user] ## remove user from user list
            session['username'] = None
    return render_template('login.html')

"""This function is called when a user clicks on a video they want to watch"""
@node.route('/<user><title>', methods=['POST'])
def watch(user, title):
    ##contact backend to pull video from holder 
    return render_template('player.html', user=user, title=title)
    
@node.errorhandler(405) #bad url
def method_not_allowed(error):
    return render_template('error.html') #send to login page

if __name__ == "__main__":
	node.secret_key = os.urandom(15)
	node.run(host='0.0.0.0')

