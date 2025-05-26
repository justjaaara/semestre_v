/*
* 1. Reciba un menu semanal (lista de recetas por dia)
* 2. Verifique los ingredientes disponibles en inventario
* 3. Calcule la lista de compras con cantidades agregadas de lo que falta.
* 4. Opcional: Clasifique los productos por categoria (e.g., frutas, carnes, lacteos, etc.)
* */
import java.util.*;
public class Main {
    static List<Ingrediente> INVENTARIO = new ArrayList<>();
    static Map<String, Receta> MENU_SEMANAL = new HashMap<>();

    public static void main(String[] args) {
        long startTimeTotal = System.nanoTime();
        
        cargarMenu();
        cargarInventario();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el dia de la semana: ");
        String dia = scanner.nextLine().toLowerCase();
        verificarInventario(dia);
        scanner.close();
        
        long endTimeTotal = System.nanoTime();
        System.out.printf("\nTiempo total del programa: %.6f segundos%n", (endTimeTotal - startTimeTotal) / 1_000_000_000.0);
    }
    static void cargarInventario() {
        INVENTARIO.add(new Ingrediente("tomate", 1, "pieza"));
        INVENTARIO.add(new Ingrediente("pasta", 100, "gramos"));
    }
    static void cargarMenu() {
        MENU_SEMANAL.put("lunes", new Receta("ensalada", Arrays.asList(
                new Ingrediente("lechuga", 1, "pieza"),
                new Ingrediente("tomate", 2, "pieza")
        )));
        MENU_SEMANAL.put("martes", new Receta("pasta", Arrays.asList(
                new Ingrediente("pasta", 200, "gramos"),
                new Ingrediente("papas", 1, "pieza")
        )));
        MENU_SEMANAL.put("miércoles", new Receta("frijoles", Arrays.asList(
                new Ingrediente("frijol", 100, "gramos"),
                new Ingrediente("cebolla", 1, "pieza"),
                new Ingrediente("platano", 1, "pieza")
        )));
        MENU_SEMANAL.put("jueves", new Receta("sopa", Arrays.asList(
                new Ingrediente("pasta", 100, "gramos"),
                new Ingrediente("tomate", 1, "pieza"),
                new Ingrediente("cebolla", 1, "pieza")
        )));
        MENU_SEMANAL.put("viernes", new Receta("tacos", Arrays.asList(
                new Ingrediente("tortilla", 2, "pieza"),
                new Ingrediente("carne", 200, "gramos"),
                new Ingrediente("tomate", 1, "pieza"),
                new Ingrediente("cebolla", 1, "pieza")
        )));
        MENU_SEMANAL.put("sábado", new Receta("pizza", Arrays.asList(
                new Ingrediente("masa", 1, "pieza"),
                new Ingrediente("tomate", 2, "pieza"),
                new Ingrediente("queso", 100, "gramos")
        )));
        MENU_SEMANAL.put("domingo", new Receta("ensalada", Arrays.asList(
                new Ingrediente("lechuga", 1, "pieza"),
                new Ingrediente("tomate", 2, "pieza")
        )));
    }
    static void verificarInventario(String dia) {
        long startTime = System.nanoTime();
        
        if (!MENU_SEMANAL.containsKey(dia)) {
            System.out.println("Día no válido.");
            return;
        }
        Receta receta = MENU_SEMANAL.get(dia);
        System.out.println("Ingredientes del dia: ");
        receta.ingredientes.forEach(ingrediente -> System.out.println(" " + ingrediente));

        long middleTime = System.nanoTime();
        
        System.out.println("Ingredientes faltantes: ");
        receta.ingredientes.stream()
            .filter(ingrediente -> {
                Ingrediente enInventario = buscarEnInventario(ingrediente.nombre);
                return enInventario == null || enInventario.cantidad < ingrediente.cantidad;
            })
            .forEach(ingrediente -> {
                Ingrediente enInventario = buscarEnInventario(ingrediente.nombre);
                if (enInventario == null) {
                    System.out.println("  Falta todo: " + ingrediente);
                } else {
                    int diferencia = ingrediente.cantidad - enInventario.cantidad;
                    System.out.println("  Faltan " + diferencia + " " + ingrediente.unidad + " de " + ingrediente.nombre);
                }
            });
            
        long endTime = System.nanoTime();
        System.out.printf("\nTiempo de verificación de inventario: %.6f segundos%n", (endTime - startTime) / 1_000_000_000.0);
        System.out.printf("Tiempo de procesamiento de ingredientes faltantes: %.6f segundos%n", (endTime - middleTime) / 1_000_000_000.0);
    }
    static Ingrediente buscarEnInventario(String nombre) {
        for (Ingrediente ingrediente : INVENTARIO) {
            if (ingrediente.nombre.equalsIgnoreCase(nombre)) {
                return ingrediente;
            }
        }
        return null;
    }
}