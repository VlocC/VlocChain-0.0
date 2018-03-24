/**
 * @author Owen Sullivan @multiojuice
 * @file Holder.java
 * This is eventually going to take in videos and host them on the machine
 * that this is being ran on. Then send them up to the webpage upon request.
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.Socket;
import java.util.Scanner;


/**
 * just a send and response server for right now,
 * This will eventually do what is stated above
 */
public class Holder {
    public static void main(String[] args) throws IOException {
        Socket client = new Socket("localhost",6789);
        DataInputStream inputStream = new DataInputStream(client.getInputStream);
        FileOutputStream writer = new FileOutputStream("random.txt");
        byte[] info = new byte[4096]

        // Preparing to send out videos again!

        bufferedReader.close();
        printStream.close();
        client.close();
    }
}
