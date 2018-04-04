package Server;

import Utils.IpObject;

import java.io.File;
import java.io.IOException;

import static Server.Controller.videoMap;

public class FileMonitor implements Runnable{

    public static final String DIRECTORY = "/home/multiojuice/VlocChain/newVideos/";

    @Override
    public void run() {

        while(true) {

            File temp = checkForNewVideos();
            if (temp != null) {
                System.out.println("Sending " + temp);

                IpObject ip = Controller.ipSet.first();
                ip.setVideoNumber();
                VideoUploader videoUploader = null;

                try {
                    videoUploader = new VideoUploader(temp,ip.getAddr());
                    videoMap.put(temp.getName(),ip.getAddr());
                } catch (IOException e) {
                    e.printStackTrace();
                }

                Thread thread = new Thread(videoUploader);
                thread.start();
            }

            try {
                Thread.sleep(1);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public static File checkForNewVideos() {

        File dir = new File(DIRECTORY);
        File[] dir_contents = dir.listFiles();
        if(dir_contents == null || dir_contents.length <= 0 ) return null;
        return dir_contents[0];
    }

}
