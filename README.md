# VlocChain

## Overview

#### Origin
VlocChain and the idea of it was created in a hurried brainstorming session at RIT's Brickhack 4. Our team wanted to mess around and do something with the idea of blockchain. The first few hours of the 24 hour hackathon were spend researching about blockchain and how we could actually implement it. This was our first step, and the start of VlocChain.

#### Original Idea
The original idea was to be able to send videos from computer to computer as "Tokens" or "Vloccs", we would track it with a ledger that was distributed and updated through every node in the chain. Each Vlocc would have to mined and we used a sort of standard proof of work for the mining, we practically just wanted to have the most standard, custom blockchain we could make, but for some reason also have it send things :). At the actual hackathon, the technology being used was http requests, python3, and flask. In the end, we were doing most of everything we wanted to do, but we thought we could extend this to be a much cooler and more impressive system. 

#### Current Vision
**Now**, our team is working to create a webpage that hosts videos for people to view, however we hope for it to not be like an ordinary video hosting website. VlocChain and it's videos will be distributed across several nodes, any computer that wants to be a node, and our page will pull it and host it there. The program will keep track of where every video is using ledgers like all blockchains do. Once a video hits a threshold of views, the Video will be created into a 'Vlocc', or the block object. This threshold will be like our proof of work. The benefit of this being a vlocc will mean that this video will be eligible for certain perks to come in the future!! We are still figuring out the ideas and how to do them, but you shall be updated soon!

##### Current Vision ~ Future Developments
- Much more, but these are things to come in the very near future!

## What does each file do?

#### Front End


#### Back End
##### The Controller
-[Link](/BackEnd/)

-Funcitonality
  1. Takes files in *newVideos/* and distributes them to the known and connected holders
  2. Keeps track of nodes and keeps our map of videos up to date
  3. Pulls the video back to the web client upon a web request for viewing

- Misc 
  1. This is ran side by side with the web server.

##### Holders
- [Link](/BackEnd/)

##### Tools
- NGINX, used as our overarching web server.
- uWSGI, to link our app to NGINX and tell it just how to do it.
- Flask, the web framework that runs our app.
- Java, what the Controller and Holders are written in.

## Becoming a Holder
Take a look at our becoming a holder page on the website! (To be implemented soon)

#### What are the benefits?
Well, right now, nothing. **However**, we plan to give a portion of the benefits given to the Video owners to the holder that is hosting these Videos. This way, there will be growing interest in becoming a holder and hosting part of the VlocChain in the same rate that interest in making videos raise! This is what holds up our system and our ideas! More details will be availble in the future!

#### Initialization
1. Download or clone our Holder repository to your local computer. Java must be downloaded to run the program.
2. Follow the step by step guide on that repository linked [here](). 
3. **Future**, you will have to input max storage you are willing to lend to the VlocChain, along with how much traffic you are willing to take in at once and send at once. There will be minimums, but we have not decided these yet. :)

