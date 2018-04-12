package Server;

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
public class RecallMonitor implements Runnable{

    // The directory to search
    public static final String DIRECTORY = "/home/vlocc/recallDir";

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
		System.out.println("Recalling -> " + temp.getName());
		
		String IP_location = null;

		try{
  		    String query = "SELECT * FROM video_locations WHERE video_name = '"
			    + temp.getName()
			    + "'";
		    Statement st = Controller.conn.createStatement();
		    ResultSet rs = st.executeQuery(query);
		    rs.next();
		    IP_location = rs.getString("IP_location").substring(1);
		    System.out.println("Recalling from -> " + IP_location);
		    st.close();		    
		} catch (SQLException e) {
		    e.printStackTrace();
		}

		RecallVideo recall = null;
		try {
		    recall = new RecallVideo(temp.getName(), IP_location);
		} catch (IOException e) {
		    e.printStackTrace();
		}
		Thread thread = new Thread(recall);
		thread.start();
		temp.delete();
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
