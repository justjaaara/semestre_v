case class Vehiculo(id: Int, marca: String, modelo: String, año: Int, precio: Double)
case class Venta(id: Int, vehiculo: Vehiculo, vendedor: String, cliente: String)

//def calcularTotalDeVentasPorMarca(ventas : List[Venta]): Int = {
//
//}
//


@main
def main(): Unit =
  val ventas = List(Venta(1, Vehiculo(101, "Toyota", "Corolla Cross", 2025, 7000),"Juan", "Gui"),
                    Venta(2, Vehiculo(102, "Honda", "Civic", 2023, 25000),"Luis", "P"),
                    Venta(3, Vehiculo(103, "Ford", "Mustang", 2021, 45000),"Sara", "Falta"),
                    Venta(4, Vehiculo(104, "Tesla", "Model 3", 2022, 60000), "Sofí", "a"),
                    Venta(5, Vehiculo(105, "Chevrolet", "Camaro", 2020, 38000), "Diego", "Roberto"),
    Venta(6, Vehiculo(106, "Toyota", "RAV4", 2024, 30000), "Ana", "Luis"),
    Venta(7, Vehiculo(107, "Hyundai", "Elantra", 2023, 22000), "Mario", "Marta"),
    Venta(7, Vehiculo(107, "Hyundai", "Elantra", 2023, 22000), "Carlos", "Marta"),
    Venta(8, Vehiculo(108, "Kia", "Sportage", 2025, 35000), "Laura", "Javier"),
    Venta(9, Vehiculo(109, "Mazda", "CX-5", 2022, 40000), "Pedro", "Sofia"),

                    )
  val numeros = List(1,2,3,4,5,6,7,8)
  val agrupados = numeros.groupBy(n => if (n%2 == 0) "par" else "impar")
  println(agrupados)

