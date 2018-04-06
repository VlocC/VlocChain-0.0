package Server;


import java.io.*;
import java.net.InetAddress;
import java.net.Socket;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class VideoUploader implements Runnable {

    private File file;
    private Socket socket;
    public VideoUploader(File file, InetAddress addr) throws IOException {
        this.file = file;
        this.socket = new Socket(addr,6789);
    }

    @Override
    public void run() {

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
            printStream.println(Controller.NEW_VIDEO);
            bufferedReader.readLine();
            printStream.println(file.getName());
            bufferedReader.readLine();
        } catch (IOException e) {
            e.printStackTrace();
        }

        try {
            this.sendVideo();
            this.socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void sendVideo() throws IOException {

        byte[] data = null;
        Path path = Paths.get(file.getPath());
        try {
            data = Files.readAllBytes(path);
        } catch (IOException e) {
            e.printStackTrace();
        }

        DataOutputStream dataOutputStream = new DataOutputStream(socket.getOutputStream());
        dataOutputStream.write(data);

        // get rid of the file
        file.delete();
        System.out.println("Uploaded");

    }
}
