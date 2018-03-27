package Client;

import java.net.Socket;

public class VideoDownloader implements Runnable{

    private Socket socket;


    public VideoDownloader(Socket socket) {
        this.socket = socket;
    }

    @Override
    public void run() {

    }
}
