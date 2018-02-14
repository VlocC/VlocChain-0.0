import socket


def exchange(s):
    s.send(str.encode("Exchange"))
    s.send(str.encode("sender"))
    s.send(str.encode("reciever"))



def main():
    s = socket.socket()
    host = "127.0.0.1"
    port = 50007
    s.connect((host,port))
    command = input("input exchange")
    
    if command == "exchange":
        exchange(s)
    print("Complete")

main()
