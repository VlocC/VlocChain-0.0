package Server;

import Utils.IpObject;

import java.io.File;
import java.io.IOException;

import static Server.Controller.videoMap;

/**
 * @author Owen Sullivan
 * @file FileMonitor.java
 * A Constantly running thread, created upon the start of the controller
 * Simply checks if there are any new videos to distribute.
 * If there are, they create a video uploader for that file.
 */
public class FileMonitor implements Runnable{

    // The directory to search
    public static final String DIRECTORY = "/home/multiojuice/VlocChain/newVideos/";


    /**
     * The method called upon the threads start
     * Loops infinitely, checking for files.
     */
    @Override
    public void run() {

        // Just keep looping
        while(true) {

            // Check for a new video
            File temp = checkForNewVideos();
            if (temp != null) {
                // Notify the console
                System.out.println("Sending " + temp);

                // Get the most available holder
                IpObject ip = Controller.ipSet.first();
                // Increment the videos current storage
                ip.setVideoNumber();
                VideoUploader videoUploader = null;

                try {
                    // Start a thread to deal with the new video
                    videoUploader = new VideoUploader(temp,ip.getAddr());
                    // Track where this video is put,
                    // TODO put this into a database
                    videoMap.put(temp.getName(),ip.getAddr());
                } catch (IOException e) {
                    e.printStackTrace();
                }

                // Run the new thread
                Thread thread = new Thread(videoUploader);
                thread.start();
            }

            try {
                // Wait 15 seconds before searching again.
                Thread.sleep(15000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

        }
    }


    /**
     * Sees if there is anything the DIRECTORY
     * @return the first file found as a FILE object
     */
    public static File checkForNewVideos() {

        File dir = new File(DIRECTORY);
        File[] dir_contents = dir.listFiles();
        if(dir_contents == null || dir_contents.length <= 0 ) return null;
        return dir_contents[0];
    }

}
