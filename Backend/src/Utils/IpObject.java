package Utils;

import java.net.InetAddress;
import java.util.Objects;

/**
 * @author Owen Sullivan
 * @file IpObject.java
 * This is just an object that we store.
 * Keeps track of holder details and will be used more in
 * the future to customize how many videos a holder can store and send
 */
public class IpObject {

    // The IP address of the holder
    private final InetAddress addr;
    // How many videos do they currently hold
    private int videoNumber;


    /**
     * Init the variables
     * @param addr the ip
     * @param videoNumber how many videos the holder has currently
     */
    public IpObject(InetAddress addr, int videoNumber) {
        this.addr = addr;
        this.videoNumber = videoNumber;
    }


    /**
     * Increment the video count by one
     * Will be in bytes eventually
     */
    public void setVideoNumber() {
        this.videoNumber += 1;
    }


    /**
     * get the Ip
     * @return the holders IP
     */
    public InetAddress getAddr() {
        return addr;
    }


    /**
     * get the total storage
     * @return number of videos
     */
    public int getVideoNumber() {
        return videoNumber;
    }


    /**
     * Equals function, for our hashing
     * @param o the object to compare
     * @return if they are the same holder
     */
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof IpObject)) return false;
        IpObject ipObject = (IpObject) o;
        return videoNumber == ipObject.videoNumber &&
                Objects.equals(addr, ipObject.addr);
    }


    /**
     * Hash for this objects hashmap
     * @return the hash of the Ip and storage
     */
    @Override
    public int hashCode() {
        return Objects.hash(addr, videoNumber);
    }
}
