"""
VlocChain
Authors: Owen Sullivan, ____
Desc- Client/user interface but with sockets
file- socket_interface.py
"""

import socket


HOST = "127.0.0.1"
PORT = 50007

s = socket.socket()
s.connect((HOST,PORT))
def main():

    print("Welcome to VlocChain's user experience")
    response = input("Please enter 'new' if you are a new user")
    username = ""
    #If they need to create a new user
    if(response == "new" or response == "New"):
        #Send keyword "new" and recieve username back
        s.send(str.encode("new"))
        username = s.recv(1024).decode("utf-8")
        print("Your username is: ", response)   
        
    #If they have an acccount
    else:
        #While their username hasn't been verified
        while(True):

            username = input("Enter your username")
            #send the users username now
            s.send(str.encode(response))
            #Recieve the response True or False, if it exists
            response = s.recv(1024).decode("utf-8")
            
            if(response == "True"): break

    # At this point, the user should either have a new username or be verified
    while(True):
        direction = input("Input your desired actions (type one of the following):transaction, view, exit")
        if(direction == "exit"):
            s.send(str.encode("exit"))
            break
        elif(direction == "view"):
            view(username)
        elif(direction == "transaction"):
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
        s.send(str.encode(reciever))
        #check if it is verified
        response = s.recv(1024).decode("utf-8")
        if(response == "True"): break;
    
    #Both users verified, chose the file to send
    filename = input("input a file to send")
    s.send(str.encode(filename))
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

main()




