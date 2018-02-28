"""
VlocChain
Authors: Owen Sullivan
File- node.py
Desc- This interacts with the server class controller, 
controller will distribute videos and Vloccs across
to all the Nodes. Eventually trying to keep them even and 
maybe get rid of the controller class
"""

import socket

def download_vid(s):
    
    s.send(str.encode("download"))
    filename = s.recv(1024).decode("utf-8")
    fd = open("./nodeVideos/"+filename,"wb")
    info = s.recv(1024)
    while(info):
        print("Recieving")
        fd.write(info)
        info = s.recv(1024)
        
    fd.close()
    s.shutdown(socket.SHUT_WR)
    s.close()



def main():
    s = socket.socket()
    host = "127.0.0.1"
    port = 50007
    s.connect((host,port))
    command = input("input download")
    
    if command == "download":
        download_vid(s)
    print("Complete")

main()
