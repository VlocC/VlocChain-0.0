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









