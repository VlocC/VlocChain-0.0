package Utils;

import java.net.InetAddress;
import java.util.Objects;

public class IpObject {
    private final InetAddress addr;
    private int videoNumber;

    public IpObject(InetAddress addr, int videoNumber) {
        this.addr = addr;
        this.videoNumber = videoNumber;
    }

    public void setVideoNumber() {
        this.videoNumber += 1;
    }

    public InetAddress getAddr() {
        return addr;
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
                Objects.equals(addr, ipObject.addr);
    }

    @Override
    public int hashCode() {

        return Objects.hash(addr, videoNumber);
    }
}
