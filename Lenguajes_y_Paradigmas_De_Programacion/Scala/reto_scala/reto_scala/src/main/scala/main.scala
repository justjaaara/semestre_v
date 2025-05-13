case class Vehiculo(id: Int, marca: String, modelo: String, año: Int, precio: Double)
case class Venta(id: Int, vehiculo: Vehiculo, vendedor: String, cliente: String)

def totalVentasPorMarcas(ventas: List[Venta]): Map[String, Double] = {
  ventas.groupBy(_.vehiculo.marca)
    .map { case (marca, ventas) =>
      val total = ventas.map(_.vehiculo.precio).sum
      (marca, total)
    }
}

def vehiculosCaros(ventas: List[Venta]): List[Vehiculo] = {
  ventas.filter(_.vehiculo.precio > 30000000).map(_.vehiculo)
}

// Encontrar el vehículo más caro vendido usando reduce en el último año vigente.

// Ordenar las ventas por año del vehículo de más reciente a más antiguo usando sortBy.

// Generar un reporte en formato JSON con las estadísticas generadas.


@main
def main(): Unit =
  val ventas = List(Venta(1, Vehiculo(101, "Toyota", "Corolla Cross", 2025, 7000),"Juan", "Gui"),
                    Venta(2, Vehiculo(102, "Honda", "Civic", 2023, 25000),"Luis", "P"),
                    Venta(3, Vehiculo(103, "Ford", "Mustang", 2021, 45000),"Sara", "Falta"),
                    Venta(4, Vehiculo(104, "Tesla", "Model 3", 2022, 60000), "Sofí", "a"),
                    Venta(5, Vehiculo(105, "Chevrolet", "Camaro", 2020, 38000), "Diego", "Roberto"),
    Venta(6, Vehiculo(106, "Toyota", "RAV4", 2024, 30000), "Ana", "Luis"),
    Venta(7, Vehiculo(107, "Hyundai", "Elantra", 2023, 60000000), "Mario", "Marta"),
    Venta(7, Vehiculo(107, "Hyundai", "Elantra", 2023, 22000), "Carlos", "Marta"),
    Venta(8, Vehiculo(108, "Kia", "Sportage", 2025, 35000), "Laura", "Javier"),
    Venta(9, Vehiculo(109, "Mazda", "CX-5", 2022, 40000), "Pedro", "Sofia"),

                    )

  // Calcular el total de ventas por marca
  val totalPorMarca = totalVentasPorMarcas(ventas)
  println("Total de ventas por marca: ")
  totalPorMarca.map(x => println(s"Marca: ${x._1}, Total: ${x._2}"))

  // Filtrar vehículos caros
  val vehiculosCarosList = vehiculosCaros(ventas)
  println("Vehículos caros vendidos: ")
  vehiculosCarosList.map(x => println(s"Vehículo: ${x.marca} ${x.modelo}, Precio: ${x.precio}"))

