import scala.io.StdIn._
import java.time.Instant

case class Ingrediente(nombre: String, cantidad: Double, unidad: String)
case class Receta(nombre: String, ingredientes: List[Ingrediente])

val inventario: List[Ingrediente] = List(
  Ingrediente("tomate", 1, "pieza"),
  Ingrediente("pasta", 100, "gramos")
)

val menuSemanal: Map[String, Receta] = Map(   //Map -> diccionario
  "lunes" -> Receta("ensalada", List(
    Ingrediente("lechuga", 1, "pieza"),
    Ingrediente("tomate", 2, "pieza")
  )),
  "martes" -> Receta("pasta", List(
    Ingrediente("pasta", 200, "gramos"),
    Ingrediente("papas", 1, "pieza")
  )),
  "miercoles" -> Receta("frijoles", List(
    Ingrediente("frijol", 100, "gramos"),
    Ingrediente("cebolla", 1, "pieza"),
    Ingrediente("platano", 1, "pieza")
  )),
  "jueves" -> Receta("sopa", List(
    Ingrediente("pasta", 100, "gramos"),
    Ingrediente("tomate", 1, "pieza"),
    Ingrediente("cebolla", 1, "pieza")
  )),
  "viernes" -> Receta("tacos", List(
    Ingrediente("tortilla", 2, "pieza"),
    Ingrediente("carne", 200, "gramos"),
    Ingrediente("tomate", 1, "pieza"),
    Ingrediente("cebolla", 1, "pieza")
  )),
  "sabado" -> Receta("pizza", List(
    Ingrediente("masa", 1, "pieza"),
    Ingrediente("tomate", 2, "pieza"),
    Ingrediente("queso", 100, "gramos")
  )),
  "domingo" -> Receta("ensalada", List(
    Ingrediente("lechuga", 1, "pieza"),
    Ingrediente("tomate", 2, "pieza")
  ))
)

def verificar_cantidad_ingredientes(ingredientes: List[Ingrediente]): List[Ingrediente] = {
  val startTime = System.nanoTime()
  
  val resultado = ingredientes.map { ingrediente =>  //Cada ingrediente de la lista
    inventario.find(_.nombre == ingrediente.nombre) match {    //Mismo que swich
      case Some(item) =>
        val diferencia = ingrediente.cantidad - item.cantidad
        if (diferencia > 0)
          Ingrediente(ingrediente.nombre, diferencia, ingrediente.unidad)
        else
          null  // Ya hay suficiente en inventario
      case None =>
        ingrediente  // No hay nada en inventario
    }
  }.filter(_ != null)
  
  val endTime = System.nanoTime()
  println(f"\nTiempo de verificación de ingredientes: ${(endTime - startTime) / 1_000_000_000.0}%.6f segundos")
  
  resultado
}

def verificarInventario(dia: String): Unit = {
  val startTime = System.nanoTime()
  
  menuSemanal.get(dia.toLowerCase) match {
    case Some(receta) =>
      println(s"Receta para $dia: ${receta.nombre}")
      println("Ingredientes del día:")
      receta.ingredientes.foreach(println)
      val faltantes = verificar_cantidad_ingredientes(receta.ingredientes)
      println("\nIngredientes faltantes:")
      faltantes.foreach(println)
    case None =>
      println("Día inválido.")
  }
  
  val endTime = System.nanoTime()
  println(f"\nTiempo de verificación de inventario: ${(endTime - startTime) / 1_000_000_000.0}%.6f segundos")
}

@main
def main(): Unit = {
  val startTimeTotal = System.nanoTime()
  
  print("Ingrese el día de la semana: ")
  val dia_semana = readLine()
  verificarInventario(dia_semana)
  
  val endTimeTotal = System.nanoTime()
  println(f"\nTiempo total del programa: ${(endTimeTotal - startTimeTotal) / 1_000_000_000.0}%.6f segundos")
}