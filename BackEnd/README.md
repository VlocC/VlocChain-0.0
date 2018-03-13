# Backend

### Overview

This is the folder holding a few files that will practically be always running. The idea of this is to have on controller that runs on the same system as the web server. This will take the new videos uploaded to our site, and distribute them across the nodes on the network. Once a user requests to watch a video(on the web page), the controller will ping the correct node and have that node send the video to the user so that it may be watched.
There are many ways we are looking to implement this and the team is super excited for the outcome! Each node will have a database to hold their videos and other information. 


### Current Plan

Well right now, I am mainly planning on how I want to do this. I have decided I am actually going to write this stuff using java rather than python. This is for a few reasons, a few being that Java's Multithreading outclasses Python's by a mile. Second, the serialization in java will serve as a useful tool I'd like to use, on top of this, I am trying to explore Java more and this is a great opportunity to see the full capabilities of Java's tools!

With this planning, I am writing a lot of background tests and sample programs to try and get familiar with java's version of the python tools I have been using.
#### To Do

1. Enable the controller to be monitoring for new nodes/connections.
2. Send videos and pictures between nodes and controller.
3. Create objects to store all video information, send this full object.
4. Multithread the entire system to allow more nodes to join the network.
5. Create a system to find the node with the desired video, and then send it up to the user.
