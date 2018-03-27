package Server;

import java.io.DataOutputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.net.Socket;

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
        out = new DataOutputStream(client.getOutputStream());
        inputStream = new FileInputStream(file);
    }

    public void setThreadName(String threadName) {
        this.threadName = threadName;
    }



    // What the thread should runF
    @Override
    public void run() {


    }
}


