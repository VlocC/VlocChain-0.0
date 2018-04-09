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
import java.net.InetAddress;
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

    // Standardized messages to comunicate between controller and holder
    public static final String NEW_VIDEO = "new_video";
    public static final String RECALL = "recall";
    // Data structures to keep track of all holders
    // And where our videos are
    // TODO turn this into DB
    public static HashMap<String,InetAddress> videoMap;
    public static TreeSet<IpObject> ipSet;

    public static void main(String[] args) throws IOException{

        // Initialize the variables
        videoMap = new HashMap<>();
        ipSet = new TreeSet<>(Comparator.comparingInt(IpObject::getVideoNumber));

        // Create our server socket to get connections
        ServerSocket serverSocket = new ServerSocket(10000);
        // Alert the console
        System.out.println("Server Running");

        // Wait for at least one connection before we start sending files
        Socket clientSocket1 = serverSocket.accept();
        // Add the IP object to our data structures
        IpObject ipObject1 = new IpObject(clientSocket1.getInetAddress(),0);
        ipSet.add(ipObject1);
        // Alert the console
        System.out.println("Connected to the first holder");

        // Create the FileMonitor
        FileMonitor fileMonitor = new FileMonitor();
        Thread monitorThread = new Thread(fileMonitor);
        monitorThread.start();

        // Keep connecting to new holders
        while(true) { // Loop and look for new connections
            // Accept a new connection
            Socket clientSocket = serverSocket.accept();
            IpObject ipObject= new IpObject(clientSocket.getLocalAddress(),0);
            ipSet.add(ipObject);
            // ADD MONITORING FOR RECALLS
            // TODO add recalls
        }
    }
}
