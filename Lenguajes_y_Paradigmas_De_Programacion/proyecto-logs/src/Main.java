import java.util.List;
import java.util.concurrent.TimeUnit;

public class Main {
    public static void main(String[] args) {
        while (true) { // Bucle infinito para ejecución continua
            // Generar logs
            List<ServerLog> logs = LogGenerator.generateLogs(1000); // Generar 10 logs cada iteración

            // Procesar logs concurrentemente
            LogProcessor.processLogsConcurrently(logs);

            // Analizar logs
            LogAnalyzer.analyzeLogs(logs);

            // Esperar 5 segundos antes de la siguiente iteración
            try {
                TimeUnit.SECONDS.sleep(30); // Intervalo de 5 segundos
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("-----------------------------------------------");
        }
    }
}