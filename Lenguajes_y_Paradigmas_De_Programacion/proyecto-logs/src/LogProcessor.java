import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class LogProcessor {
    public static void processLogsConcurrently(List<ServerLog> logs) {
        ExecutorService executor = Executors.newFixedThreadPool(4);

        for (ServerLog log : logs) {
            executor.submit(() -> processLog(log));
        }

        executor.shutdown();
        try {
            executor.awaitTermination(1, TimeUnit.MINUTES);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    private static void processLog(ServerLog log) {
        // Simular procesamiento de log
        System.out.println("Procesando log: " + log);
    }
}