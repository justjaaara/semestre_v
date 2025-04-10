import java.util.Arrays;

public class Paradigmas {


    public static void main(String[] args){
        imperative();
        declarative();
    }
    public static void imperative() {
        int[] numbers = { 1, 2, 3, 4, 5};
        int sum = 0;

        // Iterar sobre los elementos del arreglo y sumarlos
        for (int i=0; i < numbers.length; i++) {
            sum += numbers[i];
        }

        // Imprimir el resultado de la suma
        System.out.println("La suma imperativa es: " + sum);
    }

    public static void declarative() {
        int[] numbers = { 1, 2, 3, 4, 5};

        int sum = Arrays.stream(numbers).sum();

        System.out.println("La suma declaratvia es: " + sum);
    }
}