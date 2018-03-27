package Client;

import java.net.Socket;

public class Recall implements Runnable{

    private Socket socket;

    public Recall(Socket socket) {
        this.socket = socket;
    }


    @Override
    public void run() {

    }
}
