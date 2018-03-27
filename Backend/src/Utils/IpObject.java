package Utils;

import java.util.Objects;

public class IpObject {
    private final String ip;
    private int videoNumber;

    public IpObject(String ip, int videoNumber) {
        this.ip = ip;
        this.videoNumber = videoNumber;
    }

    public void setVideoNumber() {
        this.videoNumber += 1;
    }

    public String getIp() {

        return ip;
    }

    public int getVideoNumber() {
        return videoNumber;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof IpObject)) return false;
        IpObject ipObject = (IpObject) o;
        return videoNumber == ipObject.videoNumber &&
                Objects.equals(ip, ipObject.ip);
    }

    @Override
    public int hashCode() {

        return Objects.hash(ip, videoNumber);
    }
}
