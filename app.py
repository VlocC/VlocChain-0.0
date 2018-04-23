"""
VlocChain
Authors: Owen Sullivan, Joe DeGrand, Carter Nesbitt
Filename: app.py
"""

from flask import Flask
from flask import request, session, render_template, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_uploads import UploadSet, configure_uploads
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from lxml import html
from werkzeug.utils import secure_filename
import json
import requests
import hashlib as hasher
import datetime as date
import random
import os
import operator
import hashlib

# import configdb
node = Flask(__name__)
# node = configdb.opendb(node)
# node.config['SQLALCHEMY_DATABASE_URI'] = configdb.opendb(node)
node.config.from_pyfile('db.cfg')
db = SQLAlchemy(node)
from model import *
videos = UploadSet('videos', ('mp4','webm','avi','mov'))
# node.config['UPLOADED_FILES_DEST'] = 'newVideos'
node.config['UPLOADS_DEFAULT_DEST'] = 'newVideos'
configure_uploads(node, videos)
UPLOAD_FOLDER = "./newVideos"
ALLOWED_EXTENSIONS = set(["mp4", "avi", "webm"])
#node.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
videoEXTS = ['webm', 'mp4', 'mov', 'avi']
pictureEXTS=['png', 'jpg', 'jpeg']
login_manager = LoginManager()
login_manager.init_app(node)


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
RECALL_DIRECTORY = "/home/vlocc/recallDir/"

"""
When this place gets pinged, make a new user and send the information
out so the pinger can recieve it
"""


"""
The home page of the website. If the user isn't logged in yet, it will bring them to the login page. Otherwise, the hub page will be rendered.
"""
@node.route('/', methods=['GET', 'POST'])
def index():
    # if not session.get('logged'): #If the user is not logged in
    if current_user.is_authenticated:
        return redirect('/home')
    else: #If the user is logged in
        return render_template('login.html')

"""
The form from "login.html", sent when the user clicks the "submit" button
"""
@node.route('/login', methods=['POST'])
def check_user():
    if request.method == "POST":
        usern = request.form['username']
        obj = db.session.query(User).filter_by(username=usern).first()
        pwd = hashlib.sha256((request.form['password']).encode('ascii')).hexdigest()
        if obj == None:
            return redirect('/register')
        else:
            if obj.password == pwd:
                login_user(obj)
                return redirect('/home')
            else:
                return redirect('/register')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@node.route('/home', methods=['GET', 'POST'])
@login_required
def feed():
    #vid_list = []
    vid_list = db.session.query(Video).order_by(desc(Video.id)).limit(9).all()
    #current_user = current_user.get_id()
    #for i in range(1, 10):
     #   vid_list = [db.session.query(Video).get(i)]
    # vids = vid.statement.execute().fetchall()
    #for video in vid:
    #    vid_list += [video]
    
    #return render_template('feed.html', vid_list=vid_list, current_user=current_user)
    return render_template('feed.html', vid_list=vid_list)
    # return render_template('feed.html')

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
        first = request.form['first_name']
        last = request.form['last_name']
        pwd = hashlib.sha256((request.form['password']).encode('ascii')).hexdigest()
        rpwd = hashlib.sha256((request.form['confirm_password']).encode('ascii')).hexdigest()
        mail_address = request.form['email']
        if pwd == rpwd:
            new_user = User(username=userr, first_name=first, last_name=last, email=mail_address, password=pwd)
            db.session.add(new_user)
            db.session.commit()
            # mysql.execute("insert into info values('" + userr + "','" + "'test', 'testlast', '" + mail_address + "','" + pwd + "'")
            return redirect("/")
        else:
            return "The passwords didn't match!"

"""Returns user to login page after logging out of an account"""
@node.route('/logout', methods=['POST','GET'])
@login_required
def logout():
    logout_user()
    # return json.dumps({'logging_out':'OK'})
    return redirect("/")
    # session['logged'] = False
    # session['username'] = None
    # return redirect("/")


@node.route('/upload', methods=['POST','GET'])
@login_required
def upload():
    return render_template('upload.html')


@node.route('/upload_video', methods=['POST'])
@login_required
def upload_video():
    if request.method == "POST":
        vid_title = request.form['title']
        desc = request.form['description']
        #file = request.files.getlist('file')
        video_file = request.files['video_file']
        picture_file = request.files['picture_file']
        user = current_user.username
        vfilename = video_file.filename.lower().split('.')
        vext = vfilename[-1]
        pfilename = picture_file.filename.lower().split('.')
        pext = pfilename[-1]
        if vext in videoEXTS:
            new_video = Video(title=vid_title, creator=user, description=desc, extension=vext)
            db.session.add(new_video)
            db.session.commit()
            video_file.save('./newVideos/' + user + "-" + vid_title + "." + vext)
        if pext in pictureEXTS:
           picture_file.save('./static/thumbnails/' + user + "-" + vid_title + "." + "jpg")

        """
        for f in file:
            filename = f.filename.lower().split('.')
            ext = filename[-1]
            if ext in videoEXTS:
                new_video = Video(title=vid_title, creator=user, description=desc, extension=ext)
                db.session.add(new_video)
                db.session.commit()
                f.save('./newVideos/' + user + "-" + vid_title + "." + ext)
            else:
                f.save('./static/thumbnails/' + user + "-" + vid_title + "." + ext)
            #filename = videos.save(request.files['media'])
            #file.save('./newVideos')
    """
    return redirect('/upload')

"""This function is called when a user clicks on a video they want to watch"""
@node.route('/video/<user>/<video>', methods=['POST', 'GET'])
def watch(user,video):
        
    video_name = user+"-"+video+".mp4"

    f = open(RECALL_DIRECTORY  + video_name, "w+")
    f.close()
    video_path = "/static/StreamingVideos/" + video_name
    
    fileExists = os.path.isfile("/home/vlocc/VlocChain"+video_path)
    while(not fileExists):
        fileExists = os.path.isfile("/home/vlocc/VlocChain"+video_path)

    return render_template('player.html', video_path=video_path)

@node.route('/profile/<user>', methods=['POST','GET'])
def profile(user):
    return render_template('user-account.html', user=user)


@node.errorhandler(405) #bad url
def method_not_allowed(error):
    return render_template('error.html') #send to login page

if __name__ == "__main__":
	node.secret_key = os.urandom(15)
	node.run(host='0.0.0.0')
