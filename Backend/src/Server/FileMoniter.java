package Server;

import Utils.IpObject;

import java.io.File;
import java.io.IOException;

public class FileMoniter implements Runnable{

    public static final String DIRECTORY = "";

    @Override
    public void run() {

        while(true) {

            File temp = checkForNewVideos();
            if (temp != null) {

                IpObject ip = Controller.ipSet.first();
                ip.setVideoNumber();
                VideoUploader videoUploader = null;

                try {
                    videoUploader = new VideoUploader(temp,ip.getIp());
                } catch (IOException e) {
                    e.printStackTrace();
                }

                Thread thread = new Thread(videoUploader);
                thread.start();
            }

            try {
                Thread.sleep(15000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    private File checkForNewVideos() {

        File dir = new File(DIRECTORY);
        File[] dir_contents = dir.listFiles();
        if(dir_contents == null || dir_contents.length <= 0 ) return null;

        return dir_contents[0];
    }

}
