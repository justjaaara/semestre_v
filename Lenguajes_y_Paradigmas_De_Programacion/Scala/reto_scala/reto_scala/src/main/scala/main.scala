import play.api.libs.json._
import java.io._

case class Vehiculo(id: Int, marca: String, modelo: String, año: Int, precio: Double)
case class Venta(id: Int, vehiculo: Vehiculo, vendedor: String, cliente: String)

object MainApp{
def totalVentasPorMarcas(ventas: List[Venta]): Map[String, Double] = {
  ventas.groupBy(_.vehiculo.marca)
    .map { case (marca, ventas) =>
      val total = ventas.map(_.vehiculo.precio).sum
      (marca, total)
}

def vehiculosCaros(ventas: List[Venta]): List[Vehiculo] = {
  ventas.filter(_.vehiculo.precio > 30000000).map(_.vehiculo)
}

def vehiculoMasCaroVendido(ventas: List[Venta]): Vehiculo ={
  val vehiculosUltimoAnio = ventas.filter(_.vehiculo.año == 2025)
  vehiculosUltimoAnio.map(_.vehiculo).reduce((v1, v2) => if (v1.precio > v2.precio) v1 else v2)
}
def ordenarVentasPorAnio(ventas: List[Venta]) : List[Venta] = {
  ventas.sortBy(_.vehiculo.año)(Ordering[Int].reverse)
}

implicit val vehiculoWrites: Writes[Vehiculo] = Json.writes[Vehiculo]
implicit val ventaWrites: Writes[Venta] = Json.writes[Venta]

@main
def main(): Unit = {
  val ventas = List(Venta(1, Vehiculo(101, "Toyota", "Corolla Cross", 2025, 7000), "Juan", "Gui"),
    Venta(2, Vehiculo(102, "Honda", "Civic", 2023, 25000), "Luis", "P"),
    Venta(3, Vehiculo(103, "Ford", "Mustang", 2021, 45000), "Sara", "Falta"),
    Venta(4, Vehiculo(104, "Tesla", "Model 3", 2022, 60000), "Sofí", "a"),
    Venta(5, Vehiculo(105, "Chevrolet", "Camaro", 2020, 38000), "Diego", "Roberto"),
    Venta(6, Vehiculo(106, "Toyota", "RAV4", 2024, 30000), "Ana", "Luis"),
    Venta(7, Vehiculo(107, "Hyundai", "Tucson", 2023, 60000), "Mario", "Marta"),
    Venta(7, Vehiculo(107, "Hyundai", "Elantra", 2023, 22000), "Carlos", "Marta"),
    Venta(8, Vehiculo(108, "Kia", "Sportage", 2025, 35000), "Laura", "Javier"),
    Venta(9, Vehiculo(109, "Mazda", "CX-5", 2022, 40000000), "Pedro", "Sofia"),

  )

  // Calcular el total de ventas por marca
  val totalPorMarca = totalVentasPorMarcas(ventas)
  println("Total de ventas por marca: ")
  totalPorMarca.map(x => println(s"Marca: ${x._1}, Total: ${x._2}"))

  println("---------------------------------------------------------------------------------------------------------------")

  // Filtrar vehículos caros
  val vehiculosCarosList = vehiculosCaros(ventas)
  println("Vehículos caros vendidos: ")
  vehiculosCarosList.map(x => println(s"Vehículo: ${x.marca} ${x.modelo}, Precio: ${x.precio}"))

  println("---------------------------------------------------------------------------------------------------------------")

  // Encontrar el vehiculo mas caro vendido en el ultimo año vigente
  val v = vehiculoMasCaroVendido(ventas)
  println(s"Vehiculo más caro vendido en el último año: ${v.marca} ${v.modelo} por ${v.precio}")

  println("---------------------------------------------------------------------------------------------------------------")

  //ordenar ventas por año del más reciente al más antiguo
  val ventasOrdenadas = ordenarVentasPorAnio(ventas)
  println(s"Ventas ordenadas por año (de más reciente a más antiguo)  ")
  ventasOrdenadas.map(x => println(s"Vehículo: ${x.vehiculo.marca} ${x.vehiculo.modelo}, Año: ${x.vehiculo.año}, Precio: ${x.vehiculo.precio}"))

  //Generar un reporte en formato JSON con las estadísticas generadas.
  println("---------------------------------------------------------------------------------------------------------------")
  val reporteJson: JsValue = Json.obj(
    "totalVentasPorMarca" -> totalPorMarca,
    "vehiculosCaros" -> vehiculosCarosList,
    "vehiculoMasCaroUltimoAnio" -> Json.toJson(v),
    "ventasOrdenadasPorAnio" -> ventasOrdenadas
  )
  println("REPORTE EN FORMATO JSON")
  println(Json.prettyPrint(reporteJson))

  // Guardar en carpeta "reportes"
  val carpeta = new File("reportes")
  if (!carpeta.exists()) carpeta.mkdirs()

  val archivo = new PrintWriter(new File("reportes/reporte_ventas.json"))
  archivo.write(Json.prettyPrint(reporteJson))
  archivo.close()

  println("✅ Reporte guardado en 'reportes/reporte_ventas.json'")
}