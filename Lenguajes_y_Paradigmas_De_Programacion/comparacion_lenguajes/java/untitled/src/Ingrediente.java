public class Ingrediente {
    String nombre;
    int cantidad;
    String unidad;

    Ingrediente(String nombre, int cantidad, String unidad) {
        this.nombre = nombre;
        this.cantidad = cantidad;
        this.unidad = unidad;
    }

    @Override

    public String toString() {
        return nombre + " " + cantidad + " " + unidad;
    }
}
