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
    if(response == "new" || response == "New"):
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
    while(True):
        direction = input("Input your desired actions (type one of the following):\n
            transaction, view, exit")
        if(direction == "exit"):
            s.send(encode("exit"))
            break
        else if(direction == "view"):
            view(username)
        else if(direction == "transaction"):
            transaction(username)

    #After all actions are completed
    s.shutdown(socket.SHUT_WR)
    s.close()




def view(username):
    pass


"""
desc- sends files to another address
param- username of the sender
"""
def transaction(username):
    #get and send the recievers name to verify
    while(True):
        reciever = input("Enter the recievers address")
        s.send(encode(reciever))
        #check if it is verified
        response = s.recv(1024)
        if(response == True): break;
    
    #Both users verified, chose the file to send
    filename = input("input a file to send")
    filename = open(filename,'rb')
    #take info from file
    info = filename.read(1024)
    while(info): #while therer is info to send
        print("Sending data..")
        #send it and read more
        s.send(info)
        info = filename.read(1024)

    print("Transaction Completed")
    filename.close()
    
        

