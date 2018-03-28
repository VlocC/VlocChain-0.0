package Server;
/**
 * @author Owen Sullivan @multiojuice
 * @file Server.Controller
 * This is going to be ran in parralel with our flask
 * app. This is going to take the uploaded videos and
 * distribute them across a network of video holders.
 * Then alert the holders on when to send up a connection
 */

import Utils.IpObject;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Comparator;
import java.util.HashMap;
import java.util.TreeSet;

/**
 * Where the server socket is ran
 * creates a new client handler for all client sockets encountered
 * then it is dealt with there.
 */
public class Controller {

    public static final String NEW_VIDEO = "new_video";
    public static final String RECALL = "recall";
    public static HashMap<String,String> videoMap;
    public static TreeSet<IpObject> ipSet;


    public static void main(String[] args) throws IOException{

        videoMap = new HashMap<>();
        ipSet = new TreeSet<>(Comparator.comparingInt(IpObject::getVideoNumber));

        // Create the FileMonitor
        FileMonitor fileMonitor = new FileMonitor();
        Thread monitorThread = new Thread(fileMonitor);
        monitorThread.start();

        ServerSocket serverSocket = new ServerSocket(6789);
        System.out.println("Server Running");

        while(true) { // Loop and look for new connections
            // Accept a new connection
            Socket clientSocket = serverSocket.accept();
            IpObject ipObject= new IpObject(clientSocket.getRemoteSocketAddress().toString(),0);
            ipSet.add(ipObject);
            // ADD MONITORING FOR RECALLS


        }
    }
}


