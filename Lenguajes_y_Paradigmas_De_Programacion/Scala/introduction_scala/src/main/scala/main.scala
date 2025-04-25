import scala.io.StdIn.readLine
case class Persona(genero: String, edad: Int, placa: String)
def calcularTotal(precios: List[Double]): Double = {
  val totalSinDescuento = precios.sum
  val descuento = totalSinDescuento * 0.10
  totalSinDescuento - descuento
}

def celciusAFahrenheit(celcius: Double): Double = {
  (celcius * 9/5) + 32
}

def filtrarMayoresDeEdad(edades: List[Int]): List[Int] = {
  edades.filter(_ >= 18)
}

def filtrarMayoresConBeneficio(genero: String, edad: Int, ultimo_placa: String) : String = {
  if (genero == "Mujer" && edad >= 20 && ultimo_placa == "L") {
    "No cover"
  } else if (genero == "Hombre" && edad >= 18 && ultimo_placa == "L") {
    "No cover"
  } else {
    "Cover"
  }
}
//Entrada a discoteca para mayores de edad con mujeres mayores de 20
//con beneficio de parqueadero con la letra L (No cover) y
//  hombres mayores de 18 sin beneficio
@main
def main(): Unit = {
  println("------- Descuento ----------\n")
  val precios = List(100.0, 50.0, 25.0)
  val total = calcularTotal(precios)
  println(s"Total de la factura: $total \n")

  println("------- Celcius a Fahrenheit ----------\n")
  val temperaturaC = 25.0
  val temperaturaF = celciusAFahrenheit(temperaturaC)
  println(s"$temperaturaC Celsius es igual a $temperaturaF Fahrenheit \n")

  println("------- Filtrar mayores de edad ----------\n")
  val edades = List(15, 22, 30 ,17 ,40)
  val mayoresDeEdad = filtrarMayoresDeEdad(edades)
  println(s"Mayores de edad: $mayoresDeEdad \n")

  println("------- DISCOTECA ----------\n")
  print("Ingrese su genero (Hombre/Mujer): ")
  val genero = readLine()
  print("Ingrese su edad: ")
  val edad = readLine()
  print("Ingrese la placa del vehiculo: ")
  val placa = readLine()
  
  val respuesta = filtrarMayoresConBeneficio(genero, edad.toInt, placa.last.toString)
  print(s"Respuesta: $respuesta \n")

}