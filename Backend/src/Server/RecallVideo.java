package Server;


import java.net.InetAddress;
import java.net.Socket;
import java.io.*;

public class RecallVideo implements Runnable {

    private String fileName;
    private Socket socket;
    private final String RECALL_DIR = "/home/vlocc/VlocChain/static/StreamingVideos/";

    public RecallVideo(String fileName, String IP_location) throws IOException{
        this.fileName = fileName;
	this.socket = new Socket(InetAddress.getByName(IP_location), 60999);
    }

    @Override
    public void run(){
        PrintStream printStream = null;
	BufferedReader bufferedReader = null;
	try {
            bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
	    printStream = new PrintStream(socket.getOutputStream());
	} catch(IOException e) {
            e.printStackTrace();
	}

	try {
            assert printStream != null;
	    printStream.println(Controller.RECALL);

	    bufferedReader.readLine();

	    printStream.println(fileName);

	    bufferedReader.readLine();	
	} catch (IOException e) {
	    e.printStackTrace();
	}
	
	try {
	    this.recieveVideo();
	    this.socket.close();
	    printStream.close();
            bufferedReader.close();
	} catch (IOException e) {
	    e.printStackTrace();
	}		
    }


    private void recieveVideo() throws IOException{
	DataInputStream dataInputStream = new DataInputStream(socket.getInputStream());
        
	byte[] data = dataInputStream.readAllBytes();
	
	// Write to the streaming thing
	FileOutputStream fileOutputStream = new FileOutputStream(RECALL_DIR + fileName);
	fileOutputStream.write(data);
	
	// Close and alert console
	dataInputStream.close();
	fileOutputStream.close();
	System.out.println("Recalled -> " + fileName);
    }
}

