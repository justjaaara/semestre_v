import java.time.LocalDateTime;

public class ServerLog {
    private String ipAddress;
    private LocalDateTime timestamp;
    private String requestType;
    private int responseCode;

    public ServerLog(String ipAddress, LocalDateTime timestamp, String requestType, int responseCode) {
        this.ipAddress = ipAddress;
        this.timestamp = timestamp;
        this.requestType = requestType;
        this.responseCode = responseCode;
    }

    public String getIpAddress() {
        return ipAddress;
    }

    public LocalDateTime getTimestamp() {
        return timestamp;
    }

    public String getRequestType() {
        return requestType;
    }

    public int getResponseCode() {
        return responseCode;
    }

    @Override
    public String toString() {
        return "ServerLog{" +
                "ipAddress='" + ipAddress + '\'' +
                ", timestamp=" + timestamp +
                ", requestType='" + requestType + '\'' +
                ", responseCode=" + responseCode +
                '}';
    }
}