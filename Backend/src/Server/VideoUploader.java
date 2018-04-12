package Server;


import java.io.*;
import java.net.InetAddress;
import java.net.Socket;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * @author Owen Sullivan
 * @file VideoUploader.java
 * A thread created by FileMonitor
 * Created to deal with new videos
 * Distributes the given file to the given IP
 */
public class VideoUploader implements Runnable {

    // The file to send
    private File file;
    // The socket of the holder to send it to
    private Socket socket;


    /**
     * Creates the instance variables
     * @param file the file to send
     * @param addr the Ip of the holder
     * @throws IOException due to the new Socket
     */
    public VideoUploader(File file, String addr) throws IOException {
        this.file = file;
        this.socket = new Socket(InetAddress.getByName(addr),60999);
    }


    /**
     * The method called when the thread is started
     * Contacts and connects to the holder, then starts
     * to send the video once some of the initial data is sent
     */
    @Override
    public void run() {

        // Create our streams to contact
        PrintStream printStream = null;
        BufferedReader bufferedReader = null;
        try{
            bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            printStream = new PrintStream(socket.getOutputStream());
        } catch (IOException e) {
            e.printStackTrace();
        }

        try {
            assert printStream != null;
            // Send what type of action this thread is planning to do
            printStream.println(Controller.NEW_VIDEO);
            // Wait for contact
            bufferedReader.readLine();
            // Send the file name
            printStream.println(file.getName());
            // wait for the ok
            bufferedReader.readLine();
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Send the video and close the streams
        try {
            this.sendVideo();
            this.socket.close();
            printStream.close();
            bufferedReader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    /**
     * Sends the video to the given socket
     * @throws IOException because of sending
     */
    private void sendVideo() throws IOException {

        byte[] data = null;
        // Get the path
        Path path = Paths.get(file.getPath());
        try {
            // Read all the data
            data = Files.readAllBytes(path);
        } catch (IOException e) {
            e.printStackTrace();
        }
	System.out.println("read the files bytes");
        // Create the output stream to send it through
        DataOutputStream dataOutputStream = new DataOutputStream(socket.getOutputStream());
        // Simply write it to the socke
	System.out.println("Got the output stream");
        dataOutputStream.write(data);
	System.out.println("Sent the data");

        // Delete the file, now that it is stored else where
        file.delete();
        dataOutputStream.close();
        System.out.println("Uploaded");
    }
}
