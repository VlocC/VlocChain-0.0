"""
VlocChain
Authors~ Owen Sullivan, _
File- controller.py
Desc- This is going to be one of the two main files
This is going to be the backend side. Using sockets to update the other 
nodes and send the files over and information over.

"""

import socket

connections = []
users = {"sender":4,"reciever":3}

"""
Vlocc Objects, consisting of:


"""
class Vlocc:
    """
    Make the vlocc class. Give each vlocc 
    a unique ID.
    """

    def __init__(self):
        """
        Create init
        """
        pass



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

    s = socket.socket()

    host = ''
    port = 50007

    s.bind((host,port))
    s.listen(5)
    while(True):
        c,addr = s.accept()
        command = c.recv(1024).decode("utf-8")
        if command == "Exchange":
            sender = c.recv(1024).decode("utf-8")
            reciever = c.recv(1024).decode("utf-8")
            if sender in users and reciever in users:
                print("Success")
            else:
                print("Fail")

            

        
        


main()





