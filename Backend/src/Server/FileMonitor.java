package Server;

import Utils.IpObject;

import java.io.File;
import java.io.IOException;
import java.sql.*;

/**
 * @author Owen Sullivan
 * @file FileMonitor.java
 * A Constantly running thread, created upon the start of the controller
 * Simply checks if there are any new videos to distribute.
 * If there are, they create a video uploader for that file.
 */
public class FileMonitor implements Runnable{

    // The directory to search
    public static final String DIRECTORY = "/home/vlocc/VlocChain/newVideos/";


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

                // Get the most availble holder
                VideoUploader videoUploader = null;
		String IP_location;
		try {
	            String query = "SELECT * FROM location_storage WHERE storage_amount =  ( SELECT MIN(storage_amount) FROM location_storage )";
	            Statement st = Controller.conn.createStatement();
	            ResultSet rs = st.executeQuery(query);
	            rs.next();
	            IP_location = rs.getString("IP_location");
	            int storage_amount = rs.getInt("storage_amount");
	            System.out.println(IP_location + " : " + storage_amount);

	            st.close();	

                    // Increment the videos current storage

                    // Start a thread to deal with the new video
                    videoUploader = new VideoUploader(temp, IP_location.substring(1));
                    // Track where this video is put,
                    // TODO put this into a database
		    Statement st1 = Controller.conn.createStatement();
		    String query1 = "INSERT INTO video_locations (video_name,IP_location) VALUES ('" +
			   temp.getName()
			   + "', '"
			   + IP_location 
			   + "' );";
		    st1.executeUpdate(query1);

                } catch (IOException | SQLException e) {
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
