package Server;


import java.io.File;
import java.net.Socket;

public class VideoUploader implements Runnable {

    private File file;
    private Socket socket;

    public VideoUploader(File file) {
        this.file = file;

    }

    @Override
    public void run() {
        


    }
}
