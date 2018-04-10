package Server;

import Utils.IpObject;

import java.io.IOException;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.sql.*;
import java.util.Comparator;
import java.util.HashMap;
import java.util.TreeSet;

/**
 * Where the server socket is ran
 * creates a new client handler for all client sockets encountered
 * then it is dealt with there.
 */
public class Controller {

    // Standardized messages to communicate between controller and holder
    public static final String NEW_VIDEO = "new_video";
    public static final String RECALL = "recall";
    // Data structures to keep track of all holders
    // And where our videos are
    // TODO turn this into DB
    public static HashMap<String,InetAddress> videoMap;
    public static TreeSet<IpObject> ipSet;

    //DB Variables
    private static final String JDBC_DRIVER = "org.mariadb.jdbc.Driver";
    private static final String DB_URL = "jdbc:mariadb://localhost/users";
    private static final String USER = "";
    private static final String PASS = "";
    public static Connection conn;

    public static void main(String[] args) throws IOException, SQLException, ClassNotFoundException{


        // Initialize the variables
        videoMap = new HashMap<>();
        ipSet = new TreeSet<>(Comparator.comparingInt(IpObject::getVideoNumber));


        // Create our server socket to get connections
        ServerSocket serverSocket = new ServerSocket(10000);
        // Alert the console
        System.out.println("Server Running");

        // Connect To Database
        Class.forName(JDBC_DRIVER);
        conn = DriverManager.getConnection(DB_URL, USER, PASS);
        System.out.println("Connected to DB");

        // Wait for at least one connection before we start sending files
        Socket clientSocket1 = serverSocket.accept();
        // Add the IP object to our data structures
        IpObject ipObject1 = new IpObject(clientSocket1.getInetAddress(),0);
        ipSet.add(ipObject1);

        Statement stmt =conn.createStatement();

        String sqlStatement = "INSERT INTO location_storage (IP_location, storage_amount) "
                + "VALUES ( '"
                + clientSocket1.getInetAddress()
                + "' , 0)";


        try {
            stmt.executeUpdate(sqlStatement);
            System.out.println(sqlStatement);
            System.out.println("Connected to the first holder");

        } catch (SQLIntegrityConstraintViolationException dup){

            System.out.println("Pre-existing Ip has Returned!");

        }
        // Alert the console

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

            stmt = conn.createStatement();

            sqlStatement = "INSERT INTO location_storage (IP_location, storage_amount) "
            + "VALUES ( '"
            + clientSocket.getInetAddress()
            + "' , 0)";

        try {
            stmt.executeUpdate(sqlStatement);
            System.out.println("New Connection stored in DB");

        } catch (SQLIntegrityConstraintViolationException dup){
            System.out.println("Pre-existing Ip has Returned!");
        }
        // ADD MONITORING FOR RECALLS
        // TODO add recalls
        }
    }
}
