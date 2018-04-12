package Client;

import java.io.*;
import java.net.Socket;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

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
     */
    @Override
    public void run() {

        try {
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintStream printStream = new PrintStream(socket.getOutputStream());

            // Notify the connection we are ready to do business!
            printStream.println();
            String file = bufferedReader.readLine();
            printStream.println();
            sendVideo(file);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Sends the video to the given socket
     * @throws IOException because of sending
     */
    private void sendVideo(String file) throws IOException {

        System.out.println("Finding " + file);
        byte[] data = null;
        // Get the path
        Path path = Paths.get(Holder.DOWNLOAD_DIRECTORY + file);
        try {
            // Read all the data
            data = Files.readAllBytes(path);
        } catch (IOException e) {
            e.printStackTrace();
        }
        // Create the output stream to send it through
        DataOutputStream dataOutputStream = new DataOutputStream(socket.getOutputStream());
        // Simply write it to the socket
        dataOutputStream.write(data);

        // Delete the file, now that it is stored else where
        dataOutputStream.close();
        System.out.println("Sent the recalled video");
    }

}
