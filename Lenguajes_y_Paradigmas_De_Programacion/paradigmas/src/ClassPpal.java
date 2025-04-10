import java.util.List;

public class ClassPpal {

    public static void main(String [] args){

        // System.out.println("Hola soy JUANGUI");

        List<Integer> numbers = List.of(18, 6, 20, 15, 55, 78, 12, 9, 8);

        int counter = 0;
        for(int number : numbers) {
            if (number > 10){
                counter ++;
            }
        }
        System.out.println("Los num > que 10 son: " + counter);

        Long result = numbers.stream().filter(num -> num > 10).count();
        System.out.println("Los num > que 10 son: " + result);

    }
}
