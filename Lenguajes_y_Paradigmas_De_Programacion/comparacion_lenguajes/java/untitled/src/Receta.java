import java.util.List;

public class Receta {

    String nombre;
    List<Ingrediente> ingredientes;

    Receta(String nombre, List<Ingrediente> ingredientes) {
        this.nombre = nombre;
        this.ingredientes = ingredientes;
    }
}

