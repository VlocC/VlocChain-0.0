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


## This file holds some functions that will be called
## throughout the code in the other files of this project.


## The "Vlocc" class is important for storing all the
## information that is used when making exchanges, or
## logging data.
class Vlocc:
    ## title --> the name of the file shared,
    ## assigned by the sender

    ## author --> person sending the data to receiver

    ## index --> the index of the instance of a Vlocc,
    ## stored within itself

    ## time --> timestamp of when the instance of the
    ## Vlocc was created

    ## attachment --> what the author sent; could be
    ## a string, picture, video etc.

    ## previous_hash --> the hash of the current Vlocc;
    ## named as previous for relevance in later code

    def __init__(self, title, author, index, time, attachment, previous_hash, data):

        self.title = title
        self.author = author
        self.index = index
        self.time = time
        self.attachment = attachment
        self.previous_hash = self.create_hash()
        self.data = data

    def create_hash(self):
        # uses relevant info. of Vlocc to generate hash
        new_hash = hasher.sha256((str(self.index) + self.author).encode('utf-8'))
        new_hash = new_hash.hexdigest
        return new_hash


def create_genesis():
    ## creates the first instance of a Vlocc
    ## parameters are trivial, and index is 0.

    first_stamp = str(date.datetime.now())
    starter = Vlocc("first", "author_name", 0, first_stamp, "attachment", 
            "0", {'proof': 10, 'exchanges':[]})
    return starter

def create_identity():
    ## creates an address which will be assigned to
    ## a user upon function-call with a length of 10
    ## using numbers and letters
    identity = ""
    for strLength in range(0, 10):
        charType = random.randint(0, 3)
        if (charType == 0):
            ascii = random.randint(48, 57)
        elif (charType == 1):
            ascii = random.randint(65, 90)
        else:
            ascii = random.randint(97, 122)
        identity += chr(ascii)
    return identity



nodes = [] #All known nodes get added here
vlocchain = [] #the main chain, most updated
exchanges = [] #all the exchanges
miner_address = "yeet" #temporary
vlocchain.append(create_genesis())
users = {} #full user dictionary, id: obj

@node.route('/trans', methods=['POST'])
def exchange_vid():
        """
        The output for when an exchange occurs
        """
        
        curr_exchange = request.get_json()
        exchanges.append(curr_exchange)
        print("Test below this")
        user1 = users[curr_exchange['sender']]
        user2 = users[curr_exchange['reciever']]
        print(curr_exchange['fname'])
        print(type(curr_exchange['fname']))
        user2.set_message(curr_exchange['fname'])
        print(exchanges[-1])
        print("New Video Exchange!")    #Prints out the new exchange in the terminal
        print("TITLE:", (str(curr_exchange['sender'].encode('utf-8', 'replace'))))
        print("AUTHOR:", (str(curr_exchange['reciever'].encode('utf-8', 'replace'))))
        print("FILE:", (str(curr_exchange['fname'].encode('utf-8', 'replace'))))

        return "Exchange complete!"

@node.route('/ledger', methods=['GET'])
def get_previous():
        """
        Gets all past exchanges to show on webpage
        """
        curr_chain = vlocchain
        everything = ""
        for i in range(0, len(curr_chain)):    #Puts all of the vloccs and their
                #attributes in a string for printing on a webpage
                vlocc = curr_chain[i]
                vtitle = str(vlocc.title)
                vauthor = str(vlocc.author)
                vattachment = str(vlocc.attachment)
                total = json.dumps({"Title" : vtitle ,  " Author" : vauthor,
                    "Attachment": vattachment})
                if everything == "":
                    everything = total
                else:
                    everything+=total

        return everything       #All of the vloccs in a string

def get_chains():
    """
    desc-Recieves and returns all known vlocchains
    returns- all vlocchains from all nodes
    """
    chains = []
    for element in nodes: #loop through all nodes
        chains.append(element)
    return chains

def consensus():
    """
    desc- updates the vlocchain to the newest
    """
    chains = get_chains()
    largest_chain = vlocchain

    for element in chains:
        if len(element) > len(largest_chain):
            largest_chain = element

    #sets the vlocchain
    vlocchain = largest_chain



def proof(previous_proof):
    """
    Getting X ammount of upvotes, and you will get your blocky boy
    """
    return 10


def new_info():
    # We will get this information when the VlocCoin is mined
    return("title","author","attachment")



@node.route('/mine', methods = ['GET'])
def mine():
    """
    des- How to recieve vloccs, then send to the miner
    """
    #grab the working variables
    previous_vlocc = vlocchain[-1]
    previous_proof = previous_vlocc.data['proof']
    #next find the proof of concept
    new_proof = proof(previous_proof)
    
    #Get the variables for the new vlocc
    print(exchanges)
    exchanges.append({"from":"Vlocc","to":miner_address,"ammount":1})
    print(exchanges)
    new_index = previous_vlocc.index + 1
    new_data = {'proof':new_proof,'exchanges':exchanges}
    new_time = str(date.datetime.now())
    previous_hash = str(previous_vlocc.previous_hash)
    exchanges[:] = []
    #Get the pictures input from miner
    (new_title,new_author,new_attachment) = new_info()
    #new vlocc creation
    new_vlocc = Vlocc(new_title,new_author,new_index,new_time,
        new_attachment,previous_hash,new_data)
    vlocchain.append(new_vlocc)
    #Send information to the client
    return(json.dumps({"index":new_index,"title":new_title,"Author":new_author,
        "Time":new_time,"Previous Hash":previous_hash}))



"""
/////////////////////////////|\\\\\\\\\\\\\\\\\\\\\\\\\\
?????????????????????????CONTROLLER?????????????????????
/////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""
"""
When this place gets pinged, make a new user and send the information
out so the pinger can recieve it
"""
@node.route('/newuser', methods=['GET'])
def make_new_user():

    new_identity = create_identity()
    while(new_identity in users == False):
            new_identity = create_identity()
    new_user = user_class.User(new_identity, "null", True)
    #Adds new user ID to our user list
    users[new_identity] = new_user
    print(users)
    return json.dumps({"Identity":str(new_identity)})

@node.route('/send')
def get_transactions_parents():
    # get the initial id
    user_address = users[users.keys[0]].username
    user = users[user_address]
    user_exchanges = user.get_transactions(exchanges)
    consensus()
    
    print(user_exchanges)

@node.route('/verify', methods=['POST', 'GET'])
def verify_user():
    print("In verify")
    if request.method == 'POST':
        user_name = request.form['Username']
        result = user_name in users
        print("The result is", result)
        return json.dumps(result)

@node.route('/print', methods=['POST'])
def print_message():
    print("START OF PRINT MESSAGE")

    r = request.get_json()

    print("I AM RIGHT HERRRRRRRRRRRRRRRRRRRREEEEEE")
    print(type(r))
    print(r)
    user = users[r['username']]

    return user.message

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
