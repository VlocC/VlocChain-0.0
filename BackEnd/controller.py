"""
VlocChain
Authors~ Owen Sullivan, _
File- controller.py
Desc- This is going to be one of the two main files
This is going to be the backend side. Using sockets to update the other 
nodes and send the files over and information over.

"""

import socket
import os

# a dictionary of key of socket and val of lists with (address, how many videos
# on that nodes connection)
connections = []

#temp list of users for testing
users = {"sender":4,"reciever":3}



def consensus():
    """
    desc- Update all VlocChain (variables) and Ledger (variable)
    """
    pass


def mine():
    """
    desc- create Vlocc object, append to lists
        gather information
    """
    pass


def distribute(c,fd):
    connections[-1][2] += 1
    c[0].send(str.encode(fd))
    fd_cur = open("./newVideos/"+fd,'rb')
    info = fd_cur.read(1024)
    while(info):
        print("sending")
        c[0].send(info)
        info = fd_cur.read(1024)
    print("completed")
    fd_cur.close()
    os.remove("./newVideos/"+fd)
    c[0].close()
    

def main():
    """
    Where all of the functions will be called
    """

    #Going to implement multithreading
    s = socket.socket()

    host = ''
    port = 50007

    s.bind((host,port))
    s.listen(5)
    # Right now, Temporarily
    # Just check for files and send them
    while(True):
        c,addr = s.accept()
        command = c.recv(1024).decode("utf-8")
        connections.append([c,addr,0])
        #This is here temp
        #Will run all using multithreading, just need to learn
        # Pythons version of it :)
        if command == "download":
            for fd in os.listdir("./newVideos"):
                distribute(connections[-1],fd)
                            
           
main()





