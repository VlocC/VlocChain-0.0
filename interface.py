from user_class import *
# from vlocc import *
from flask import Flask
import requests


def send_to():
    """
    Functionality for sending attachments for other (WIP)
    """
    recieve = input("Please enter VlocC address of other user: ")
    attachment = input("Please enter what you want to send: ")
    User.send(recieve, attachment)

def make_new_user():
    """
    Pings website to create a new user
    """
    ping = requests.get("/newuser")
    print(ping)
    return ping

def main():
    dic = {}
    print("Welcome to VlocC!")
    new_user = input("Are you a new user? (y/n): ")
    if new_user == "y":
            new_name = make_new_user()
            print("Your Username/Address is", new_name)
    user_name = input("Please enter username: ")
    exchanges = dic[user_name]
    contin = "y"
    while contin == "y": # Loops until user inputs otherwise
            while True:
                    user_exchanges = User.get_transactions(exchanges)
                    userinput = input("What would you like to do today? ('help' for all options) ")
                    if userinput == "help":
                            print("send, view, last, wallet")
                    else:
                            break
            if userinput == "send":
                    send_to()
            elif userinput == "view":
                    print(user_exchanges)
            elif userinput == "last":
                    print(user_exchanges[-1])
            elif userinput == "wallet":
                    print(User.view_wallet())
            contin = input("Would you like to continue? (y/n): ") 

if __name__ == '__main__':
    main()

