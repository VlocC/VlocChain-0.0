package Client;

import java.io.*;
import java.net.Socket;

public class VideoDownloader implements Runnable{

    private Socket socket;


    public VideoDownloader(Socket socket) {
        this.socket = socket;
    }

    @Override
    public void run() {
        try {
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String fileName = bufferedReader.readLine();
            int fileSize = bufferedReader.read();
            downloadVideo(fileName, fileSize);
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    private void downloadVideo(String fileName, int fileSize) throws IOException {

        DataInputStream dataInputStream = new DataInputStream(socket.getInputStream());
        FileOutputStream fileOutputStream = new FileOutputStream(fileName);
        byte[] info = new byte[4096];

        int read;
        int totalRead = 0;
        int remaining = fileSize;
        while((read = dataInputStream.read(info, 0, Math.min(info.length, remaining))) > 0) {
            totalRead += read;
            remaining -= read;
            System.out.println("read " + totalRead + " bytes.");
            fileOutputStream.write(info, 0, read);
        }

        dataInputStream.close();
        fileOutputStream.close();
    }
}
