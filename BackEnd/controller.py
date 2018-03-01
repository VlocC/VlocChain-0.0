"""
VlocChain
Authors~ Owen Sullivan
File- controller.py
Desc- This is going to be one of the two main files
This is going to be the backend side. Using sockets to update the other 
nodes and send the files over and information over.

"""

import socket
import threading
import os

# a dictionary of key of socket and val of lists with (address, how many videos
# on that nodes connection)
connections = []

#temp list of users for testing
users = {"sender":4,"reciever":3}


class Controller(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

        
    def listen(self):
    
        self.sock.listen(5)
        while True:
            client,address = self.sock.accept()
            print("Connection to ",address)
            threading.Thread(target = distribute, args = (client,address)).start()
            

def distribute(client,address):
    """
    this distributes the videos to the nodes
    """
    print("Distribute")
    while True:
        directory = os.listdir("./newVideos")
        if(len(directory) > 0 ):
            print("Sending")
            client.send(str.encode("download")) 
            client.send(str.encode(directory[0]))
            fd_cur = open("./newVideos/"+directory[0],'rb')
            info = fd_cur.read(1024)
            while(info):
                print("sending")
                client.send(info)
                info = fd_cur.read(1024)
            client.send(str.encode("DOWNLOAD COMPLETE"))
            print("completed")
            fd_cur.close()
            os.remove("./newVideos/"+directory[0])

            

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


def main():
    """
    Where all of the functions will be called
    """
    host = ''
    port = 50007

    Controller(host,port).listen()
           
main()





