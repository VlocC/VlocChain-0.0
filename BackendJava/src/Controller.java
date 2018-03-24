/**
 * @author Owen Sullivan @multiojuice
 * @file Controller
 * This is going to be ran in parralel with our flask
 * app. This is going to take the uploaded videos and
 * distribute them across a network of video holders.
 * Then alert the holders on when to send up a connection
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.ServerSocket;
import java.net.Socket;


/**
 * Where the server socket is ran
 * creates a new client handler for all client sockets encountered
 * then it is dealt with there.
 */
public class Controller {
    public static void main(String[] args) throws IOException{
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


/**
 * The thread that is ran
 * Handles a clients connection,
 * takes the socket and gets input and sends output
 * This will be doing much more soon!
 */
class ClientHandler implements Runnable {

    private Socket client;
    private FileInputStream inputStream;
    private DataOutputStream out;
    private String threadName;

    public ClientHandler(Socket client, String file) throws IOException {

        this.client = client;
        out = new DataOutputStream(s.getOutputStream());
        inputStream = new FileInputStream(file);
    }

    public void setThreadName(String threadName) {
        this.threadName = threadName;
    }


    // What the thread should run
    @Override
    public void run() {

        byte[] info = new byte[4096];

        while (inputStream.read(info)){
            out.write(info);
        }
        System.out.println("File Sent");
        // Close our streams
        try {
            inputStream.close();
            out.close();
            client.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
