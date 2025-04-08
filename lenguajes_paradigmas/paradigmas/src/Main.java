import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;


public class Main {
    public static void main (String[] args) {
        List<Student> studients = List.of(
                new Student("Michell", 21,Gender.FEMALE),
                new Student("Ander", 21,Gender.MALE),
                new Student("Son", 21,Gender.MALE),
                new Student("Michell", 21,Gender.MALE)
        );

        //imperativa, imprimir solo los hombres imperativa
        System.out.println("\n \n Estudiantes Hombres");
        for (Student student: studients){
            if(Gender.MALE.equals(student.gender)){
                System.out.println(student);
            }
        }
        System.out.println("\n \n Estudiantes Mujeres");
        List<Student> females = new ArrayList<>();
        for (Student Student: studients){
            if (Gender.FEMALE.equals(Student.gender)){
                females.add(Student);
            }
        }
        for (Student student: females) {
            System.out.println(student);
        }

        //
        //
        //

        //-------------------------------------------
        //Imperativa
        List<Person> personas = new ArrayList<>();// Declaración de lista vacía
        for (Student studianteImp: studients){
            Person persona = new Person(studianteImp.name, studianteImp.age); // guardando solo name y age de la clase persona deshechando las de studients
            personas.add(persona);
        }
        System.out.println("\n \n Programación Imperativa tipo persona");
        for (Person person: personas){
            System.out.println(person);
        }
}

    // Convertir la lista de estudiantes en personas
    static class Person{
        private final String name;
        private final Integer age;

        public Person(String name, Integer age){
            this.name =name;
            this.age = age;
        }

        @Override
        public String toString() {
            return "Person{" +
                    "name='" + name + '\'' +
                    ", age=" + age +
                    '}';
        }
    }
    static class Student{
        private final String name; //definición de propiedades
        private final Integer age;
        private final Gender gender;

        public Student(String name, Integer age, Main.Gender gender) {
            this.name = name;
            this.age = age;
            this.gender = gender;
        }

        @java.lang.Override
        public java.lang.String toString() {
            return "Student{" +
                    "name='" + name + '\'' +
                    ", age=" + age +
                    ", gender=" + gender +
                    '}';
        }

    }
    enum Gender{
        FEMALE, MALE;
    }
}