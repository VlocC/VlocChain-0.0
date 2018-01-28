"""
VlocChain
Authors: Owen Sullivan, Joe DeGrand, Carter Nesbitt
Filename: vlocc.py
"""

from flask import Flask
from flask import request
import json
import requests
import hashlib as hasher
import datetime as date
node = Flask(__name__)


nodes = [] #All known nodes get added here
vlocchain = [] #the main chain, most updated
exchanges = [] #all the exchanges
miner_address = "yeet" #temporary
vlocchain.append(create_genesis())

@node.route('/new', methods=['POST'])
def exchange_vid():
        """
        The output for when an exchange occurs
        """
        curr_exchange = request.get_json()
        exchanges.append(curr_exchange)
        print("New Video Exchange!")    #Prints out the new exchange in the terminal
        print("TITLE:", (str(curr_exchange['title'].encode('utf-8', 'replace'))))
        print("AUTHOR:", (str(curr_exchange['author'].encode('utf-8', 'replace'))))
        print("FILE:", (str(curr_exchange['fname'].encode('utf-8', 'replace'))))
        return "Exchange complete!"

@node.route('/exchanges', methods=['GET'])
def get_previous():
        """
        Gets all past exchanges to show on webpage
        """
        curr_chain = vlocchain
        everything = ""
        for i in len(0, curr_chain):    #Puts all of the vloccs and their attributes in a string for printing on a webpage
                vlocc = str(curr_chain[i])
                vtitle = str(vlocc.title)
                vauthor = str(vlocc.author)
                vattachment = str(vlocc.attachment)
                all = "Title: " + vtitle +  "   Author: " + vauthor + "   Attachment: " + vattachment + "\n"
                everything += all
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

@node.route('/mine', methods = ['GET'])
def mine():
    """
    des- How to recieve vloccs, then send to the miner
    """
    #grab the working variables
    previous_vlocc = vlocchain[-1]
    previous_proof = previous_vlocc['proof']
    #next find the proof of concept
    new_proof = proof(previous_proof)
    
    new_data = {'proof':new_proof,'exchanges':exchanges}
    #Get the variables for the new vlocc
    exchange.append({"from":"Vlocc","to":miner_address,"ammount")
    new_index = previous_vlocc.index + 1
    new_timestamp = date.datetime.now()
    previous_hash = previous_vlocc.hash
    exchanges[:] = []
    #Get the pictures input from miner
    (new_title,new_author,new_attachment) = new_info()
    #new vlocc creation
    new_vlocc = Vlocc(new_title,new_author,new_index,new_time,
        new_attachment,previous_hash,data)
    vlocchain.append(new_vlocc)
    #Send information to the client
    return(json.dumps({"title":new_title,"Author":new_Author,
        "Time":new_time_stamp,"Previous Hash":previous_hash}))

