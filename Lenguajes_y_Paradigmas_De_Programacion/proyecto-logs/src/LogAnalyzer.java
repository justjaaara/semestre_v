import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class LogAnalyzer {
    public static void analyzeLogs(List<ServerLog> logs) {
        // Filtrar logs con código de respuesta 404
        List<ServerLog> notFoundLogs = logs.stream()
                .filter(log -> log.getResponseCode() == 404)
                .collect(Collectors.toList());

        System.out.println("Logs con código 404:");
        notFoundLogs.forEach(System.out::println);

        // Contar el número de logs por tipo de solicitud
        Map<String, Long> requestTypeCounts = logs.stream()
                .collect(Collectors.groupingBy(ServerLog::getRequestType, Collectors.counting()));

        System.out.println("Conteo de logs por tipo de solicitud:");
        requestTypeCounts.forEach((requestType, count) ->
                System.out.println(requestType + ": " + count));

        // Obtener las direcciones IP únicas
        List<String> uniqueIPs = logs.stream()
                .map(ServerLog::getIpAddress)
                .distinct()
                .collect(Collectors.toList());

        System.out.println("Direcciones IP únicas:");
        uniqueIPs.forEach(System.out::println);

        // Obtener el log más reciente
        ServerLog mostRecentLog = logs.stream()
                .max((log1, log2) -> log1.getTimestamp().compareTo(log2.getTimestamp()))
                .orElse(null);

        System.out.println("Log más reciente:");
        System.out.println(mostRecentLog);
    }
}