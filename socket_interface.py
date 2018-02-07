"""
VlocChain
Authors: Owen Sullivan, ____
Desc- Client/user interface but with sockets
file- socket_interface.py
"""

import socket


HOST = "127.0.0.1"
PORT = 50007

socket.socket()
s.connect((HOST,PORT))
def main():

    print("Welcome to VlocChain's user experience")
    response = input("Please enter 'new' if you are a new user")
    username = ""
    #If they need to create a new user
    if(response = "new" || response = "New"):
        #Send keyword "new" and recieve username back
        s.send(encode("new"))
        username = s.recv(1024)
        print("Your username is: ", response)   
        
    #If they have an acccount
    else:
        #While their username hasn't been verified
        while(True):

            username = input("Enter your username")
            #Send the keyword "user" to the server
            s.send(encode("user"))
            #send the users username now
            s.send(encode(response))
            #Recieve the response True or False, if it exists
            response = s.recv(1024)
            
            if(response = True): break

    # At this point, the user should either have a new username or be verified


        



