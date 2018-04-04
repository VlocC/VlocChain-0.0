package Client;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;

public class TestServer {
    public static void main(String[] args) {

        System.out.println("Server UP");
        try {

            ServerSocket ss = new ServerSocket(6789);

            Socket socket = ss.accept();
            InetAddress addr = socket.getLocalAddress();

            Socket newSocket = new Socket(addr, 6790);

            BufferedReader buff = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            PrintStream printStream = new PrintStream(newSocket.getOutputStream());

            System.out.println("The Client said- " + buff.readLine());

            printStream.println("Whats up- From the new socket");
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

}
