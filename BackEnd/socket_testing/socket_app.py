"""
VlocChain
Authors: Owen Sullivan, Joe DeGrand, Carter Nesbitt
Filename: app.py
"""

import hashlib as hasher
import datetime as date
import random
import user_class
import os
import socket


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
users = {"owen":0,"joey":0} #full user dictionary, id: obj


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


def controller():
    """ 
    desc - Will work with the main() of interface.py
    It is setup to do run in complete correspondence
    """ 
    s = socket.socket()
    host = ''
    port = 50007
    s.bind((host,port))
    s.listen(5)
    c,addr = s.accept()
    response = c.recv(1024).decode("utf-8")
    print(response)
    #if it is a new user
    if(response == "new"):
        username = create_identity()
        c.send(str.encode(username))
    else:
        #verify user
        if response in users:
            c.send(str.encode("True"))
            username = response
        else: c.send(str.encode("False"))
        
    #User is verified or given an ID at this point
    response = c.recv(1024).decode("utf-8")
    if(response == "transaction"):
        transaction(username,c,s)

    elif(response == "view"):
        pass

    elif(response == "exit"):
        print("Goodbye")


def transaction(username,c,s):
    """
    desc- takes in a transaction
    and copies the file to this server
    """
    while True:
        reciever = c.recv(1024).decode("utf-8")
        if(reciever in users): 
            c.send(str.encode("True"))
            break

    filename = c.recv(1024).decode("utf-8")
    fd = open(filename,"wb")
    info = c.recv(1024)
    while(info):
        print("recieving")
        fd.write(info)
        info = c.recv(1024)
    fd.close()
    print("done")


controller()
