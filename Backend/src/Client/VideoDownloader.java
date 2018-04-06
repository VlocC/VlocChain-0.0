package Client;

import java.io.*;
import java.net.Socket;

/**
 * @author Owen Sullivan
 * @file VideoDownloader.java
 * A thread created by holder.java
 * This takes a socket connection and receives data
 * With that data, it downloads a file to its file system
 * to be stored on the network
 */
public class VideoDownloader implements Runnable{

    // The socket that is connected to the server/video distributor
    private Socket socket;

    /**
     * Initialize the socket
     * @param socket main socket
     */
    public VideoDownloader(Socket socket) {
        this.socket = socket;
    }


    /**
     * The method to be ran when the thread is initialized
     *  Communicate with the server, get intial info (file name)
     *  Then it calls download files and closes all of our variables
     */
    @Override
    public void run() {
        try {
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintStream printStream = new PrintStream(socket.getOutputStream());
            // alert the server we are ready to talk
            printStream.println();
            String fileName = bufferedReader.readLine();

            // Move to next part
            printStream.println();
            downloadVideo(fileName);

            // Close our stuff
            socket.close();
            printStream.close();
            bufferedReader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    /**
     * Take in bytes from our server, then write them to a file
     * @param fileName
     * @throws IOException
     */
    private void downloadVideo(String fileName) throws IOException {

        DataInputStream dataInputStream = new DataInputStream(socket.getInputStream());

        byte[] data = dataInputStream.readAllBytes();
        System.out.println("Downloading " +fileName);
        FileOutputStream fileOutputStream = new FileOutputStream("/home/multiojuice/VlocChain/Backend/nodeVideos/"+fileName);
        fileOutputStream.write(data);
        fileOutputStream.close();
        dataInputStream.close();
        System.out.println("Downloaded");
    }
}
