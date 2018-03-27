package Server;


import java.io.*;
import java.net.Socket;

public class VideoUploader implements Runnable {

    private File file;
    private Socket socket;

    public VideoUploader(File file,String ip) throws IOException {
        this.file = file;
        this.socket = new Socket(ip,6789);
    }

    @Override
    public void run() {

        PrintStream printStream = null;
        try {
            printStream = new PrintStream(socket.getOutputStream());
        } catch (IOException e) {
            e.printStackTrace();
        }

        assert printStream != null;
        printStream.print(Controller.NEW_VIDEO);
        System.out.println(file.getName());
        printStream.print(file.getName());
        printStream.print((int)file.getTotalSpace());

        try {
            this.sendVideo();
            this.socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void sendVideo() throws IOException {

        FileInputStream fileInputStream = null;

        try {
            fileInputStream = new FileInputStream(file);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        DataOutputStream dataOutputStream = new DataOutputStream(socket.getOutputStream());
        byte[] info = new byte[4096];

        while(fileInputStream.read(info) > 0) dataOutputStream.write(info);

        fileInputStream.close();
        dataOutputStream.close();

    }
}
