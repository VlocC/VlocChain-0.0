package Server;
/**
 * @author Owen Sullivan @multiojuice
 * @file Server.Controller
 * This is going to be ran in parralel with our flask
 * app. This is going to take the uploaded videos and
 * distribute them across a network of video holders.
 * Then alert the holders on when to send up a connection
 */

import java.io.DataOutputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.HashMap;

/**
 * Where the server socket is ran
 * creates a new client handler for all client sockets encountered
 * then it is dealt with there.
 */
public class Controller {

    public static final String NEW_VIDEO = "new_video";
    public static final String RECALL = "recall";
    public static HashMap<String,String> videoMap;
    public static HashMap<String,Integer> ipSize;


    public static void main(String[] args) throws IOException{

        videoMap = new HashMap<>();
        ipSize = new HashMap<>();

        ServerSocket serverSocket = new ServerSocket(6789);
        System.out.println("Server Running");

        while(true) { // Loop and look for new connections
            // Accept a new connection
            Socket clientSocket = serverSocket.accept();

            // Create the handler and start it
            ClientHandler clientHandler = new ClientHandler(clientSocket,null);
            Thread thread = new Thread(clientHandler);
            clientHandler.setThreadName(thread.getName());
            thread.start();
        }
    }
}


