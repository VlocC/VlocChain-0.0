package Server;

import java.io.File;

public class FileMoniter implements Runnable{

    public static final String DIRECTORY = "";

    @Override
    public void run() {
        File temp = checkForNewVideos();
        if(temp != null) {

            VideoUploader videoUploader = new VideoUploader();

        }

        try {
            Thread.sleep(15000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    private File checkForNewVideos() {

        File dir = new File(DIRECTORY);
        File[] dir_contents = dir.listFiles();
        if(dir_contents == null || dir_contents.length <= 0 ) return null;

        return dir_contents[0];

    }




}
