package Client;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.ServerSocket;
import java.net.Socket;

public class TestClient {

    public static void main(String[] args) {
        System.out.println("Client Up");
        try {

            ServerSocket serverSocket = new ServerSocket(6790);

            Socket socket = new Socket("localhost", 6789);

            Socket newSocket = serverSocket.accept();

            PrintStream printStream = new PrintStream(socket.getOutputStream());

            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(newSocket.getInputStream()));

            printStream.println("What is up");

            System.out.println(bufferedReader.readLine());

        } catch (IOException e) {
            e.printStackTrace();

        }
    }
}
