package Client;
/**
 * @author Owen Sullivan @multiojuice
 * @file Client.Holder.java
 * This is eventually going to take in videos and host them on the machine
 * that this is being ran on. Then send them up to the webpage upon request.
 */


import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;


/**
 * just a send and response server for right now,
 * This will eventually do what is stated above
 */
public class Holder {

    public static final String NEW_VIDEO = "new_video";
    public static final String RECALL = "recall";

    public static ServerSocket serverSocket;
    public static String DOWNLOAD_DIRECTORY;

    public static void main(String[] args) throws IOException {
        DOWNLOAD_DIRECTORY = System.getProperty("user.home") + File.separator + "VlocChain" + File.separator + "Backend" + File.separator + "nodeVideos" + File.separator;
        Socket ControllerConnection = new Socket("129.21.49.139",10000);

        // This is the socket that will always be listening for new commands!
        serverSocket = new ServerSocket(60999);
        // Always be monitoring
        while(true) {

            // Get a new connection from the controller!
            Socket socket = serverSocket.accept();
            // Read in the new command
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String command = bufferedReader.readLine();
            // Depending oon the command, make a new thread to deal with the command
            switch (command) {
                // If we need to download a new video to store
                case NEW_VIDEO:
                    VideoDownloader videoDownloader = new VideoDownloader(socket);
                    Thread thread = new Thread(videoDownloader);
                    thread.start();
                    break;

                // If we need to send a video back up to the webpage
                case RECALL:
                    Recall recall = new Recall(socket);
                    Thread thread1 = new Thread(recall);
                    thread1.start();
                    break;

            }
        }
    }
}