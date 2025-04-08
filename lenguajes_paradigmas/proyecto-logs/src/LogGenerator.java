import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class LogGenerator {
    public static List<ServerLog> generateLogs(int numberOfLogs) {
        List<ServerLog> logs = new ArrayList<>();
        Random random = new Random();
        String[] requestTypes = {"GET", "POST", "PUT", "DELETE"};
        int[] responseCodes = {200, 404, 500, 403};

        for (int i = 0; i < numberOfLogs; i++) {
            String ipAddress = "192.168.1." + random.nextInt(256);
            LocalDateTime timestamp = LocalDateTime.now().minusMinutes(random.nextInt(60));
            String requestType = requestTypes[random.nextInt(requestTypes.length)];
            int responseCode = responseCodes[random.nextInt(responseCodes.length)];

            logs.add(new ServerLog(ipAddress, timestamp, requestType, responseCode));
        }

        return logs;
    }
}