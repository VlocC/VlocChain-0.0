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
    
    filename = s.recv(1024).decode("utf-8")
    fd = open("./NodeVideos/"+filename,"wb")
    info = s.recv(1024)
    while(info):
        print("Recieving")
        try:
            info.decode("utf-8") == "DOWNLOAD COMPLETE"
            break
        except UnicodeDecodeError:
            pass
        fd.write(info)
        info = s.recv(1024)
    
    print("Completed")    
    fd.close()


def main():
    s = socket.socket()
    host = "127.0.0.1"
    port = 50007
    s.connect((host,port))
    
    while True:
        action = s.recv(1024).decode("utf-8")
        if action == "download":
            download_vid(s)

    

main()
