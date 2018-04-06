package Client;

import java.net.Socket;

/**
 * @author Owen Sullivan
 * @file Recall.java
 * This is a thread created by the holder class
 * This file, upon request, sends the information back so that it can be
 * viewed on the webpage
 */
public class Recall implements Runnable{

    // The socket connected to hte main server
    private Socket socket;

    /**
     * Init the instance variables
     * @param socket the socket connected to the server
     */
    public Recall(Socket socket) {
        this.socket = socket;
    }


    /**
     * Called when the thread is started,
     * This actually sends the video back!
     * TODO Write this and figure out the connection between this and web server
     */
    @Override
    public void run() {

    }
}
