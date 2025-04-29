
def sumar1hastaN(n : Int): Int = {
  var sumatoria = 0
  for (i <- 1 to n) {
    sumatoria = sumatoria + i
  }
  sumatoria
}

def factorial(n: Int): Int = {
  if (n == 0) 1
  else n * factorial(n - 1)
}

def filtrarNumerosPares(numeros: List[Int]): List[Int] = {
  numeros.filter(num => num % 2 == 0)
}

def QuickSort(lista: List[Int]): List[Int] = {
  if (lista.length <= 1) {
    lista
  } else {
    val pivote = lista(lista.length / 2)
    val menores = lista.filter(_ < pivote)
    val mayores = lista.filter(_ > pivote)
    val iguales = lista.filter(_ == pivote)

    QuickSort(menores) ++ iguales ++ QuickSort(mayores)
  }
}

def isPrime(n: Int): Boolean = {
  if (n <= 1) return false
  for (i <- 2 to math.sqrt(n).toInt) {
    if (n % i == 0) return false
  }
  true
}

def filterPrimeAndNotPrimeNumbers(list : List[Int]): (List[Int], List[Int]) = {
  val primeNumbers = list.filter(isPrime)
  val notPrimeNumbers = list.filterNot(isPrime)
  (primeNumbers, notPrimeNumbers)
}
@main
def main(): Unit ={
  //  println("------- Sumar 1 hasta N ----------\n")
  //  print("Ingrese un numero: ")
  //  val n = readLine()
  //  val nInt = n.toInt
  //  val sumatoria = sumar1hastaN(nInt)
  //  println(s"La suma de 1 hasta $n es: $sumatoria")

  //  println("------- Factorial ----------\n")
  //  print("Ingrese un numero: ")
  //  var n = readLine()
  //  val nInt = n.toInt
  //  val resultado = factorial(nInt)
  //  println(s"El factorial de $n es: $resultado")

  println("------- Filtrar numeros pares ----------\n")
  println("Ingrese una lista de numeros separados por comas: ")
  val numeros = List(1, 2, 3, 4, 56, 7, 8, 9, 4, 5, 15, 45, 15, 4, 54, 51, 54)
  val numerosPares = filtrarNumerosPares(numeros)
  println(s"Numeros pares: $numerosPares \n")

  println("------- QuickSort ----------\n")
  val lista = List(4,3,1,2,5,9,7,10,6)
  println(s"Lista original: $lista")
  val listaOrdenada = QuickSort(lista)
  println(s"Lista ordenada: $listaOrdenada")

  println("------- Filtrar numeros primos y no primos ----------\n")
  val listaNumeros = List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
  val (primos, noPrimos) = filterPrimeAndNotPrimeNumbers(listaNumeros)
  println(s"Numeros primos: $primos")
  println(s"Numeros no primos: $noPrimos")
}


