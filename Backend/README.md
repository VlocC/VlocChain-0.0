# Backend

### Overview
This folder of files works with each other to move and host the videos that can be seen on our website.

1. [Server](./src/Server)
  * The contents of this folder are ran along side the webserver on the same VM. 
  * Everything runs out of the [Controller.java](./src/Server/Controller.java)
  * Functionality: 
    * Takes in new videos and distributes them across the holders on our network.
    * Maps where our videos are, and alerts the holder to send the wanted video to our web client.
2. [Client](./src/Client)
  * The contents of this folder are ran on seperate computers that want to be apart of the network. See [Joining the Network](#Joining the Network)
  * Anyone can download these files to run and become a part of our network. This Entails:
    * Putting our software on your computer.
    * Having videos downloaded onto your computer.
    * Traffic going through your network and computer.
  * Functionality:
    * Stores all videos uploaded to our website!
    * Sends the videos to be viewed upon a request!  

### Tools
1. Java
2. Network Sockets
3. MySQL & MariaDB

In addition to these, to actually run the java I needed to add
```
export _JAVA_OPTIONS="-Djava.net.preferIPv4Stack=true"
```
to my .bashrc. This made it possible to bind my java ServerSocket to IPv4.
### Joining the Network



### Goals

1. Automate joining the network to a simple bash script.
2. Have each 'Holder' shoot their data to the web clients directly. Rather than through our server.


