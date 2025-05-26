# Taller Comparación de Lenguajes

## ¿Cuál es el mejor?

### By Felipe, Juan Pablo, Luis P

En este taller se realiza un comparativo entre los lenguajes Java, JavaScript, Python y Scala, evaluando su rendimiento, adaptación del lenguaje y seguridad. Para ello, se desarrolló un ejercicio práctico: un Planificador Funcional de Compras Semanales.

---

## Descripción del problema

Un usuario, JuanGui, desea organizar sus compras semanales según un menú predefinido y un inventario actual. El sistema debe generar automáticamente una lista de compras, eliminando duplicados, agrupando cantidades y priorizando los ingredientes faltantes.

### Alcance

El sistema debe:

1. Recibir un menú semanal (lista de recetas por día).
2. Verificar los ingredientes disponibles en el inventario.
3. Calcular la lista de compras con cantidades agregadas de lo que falta.
4. Opcionalmente, clasificar los productos por categoría (e.g., frutas, carnes, lácteos).

### Datos de entrada y salida esperados

#### Menú semanal (JSON)

```json
[
  {
    "dia": "lunes",
    "receta": "ensalada",
    "ingredientes": [
      { "nombre": "lechuga", "cantidad": 1, "unidad": "pieza" },
      { "nombre": "tomate", "cantidad": 2, "unidad": "pieza" }
    ]
  },
  {
    "dia": "martes",
    "receta": "pasta",
    "ingredientes": [
      { "nombre": "pasta", "cantidad": 200, "unidad": "gramos" },
      { "nombre": "tomate", "cantidad": 1, "unidad": "pieza" }
    ]
  }
]
```

#### Inventario disponible

```json
[
  { "nombre": "tomate", "cantidad": 1, "unidad": "pieza" },
  { "nombre": "pasta", "cantidad": 100, "unidad": "gramos" }
]
```

#### Salida esperada: Lista de compras

```json
[
  { "nombre": "lechuga", "cantidad": 1, "unidad": "pieza" },
  { "nombre": "tomate", "cantidad": 2, "unidad": "pieza" },
  { "nombre": "pasta", "cantidad": 100, "unidad": "gramos" }
]
```

---

## Comparación de lenguajes

### Python

Python destaca por su simplicidad y rapidez en el desarrollo. Su sintaxis clara y su amplia gama de bibliotecas lo hacen ideal para prototipos rápidos y tareas ligeras. Sin embargo, su rendimiento es inferior debido a su naturaleza interpretada, y el tipado dinámico puede introducir errores en tiempo de ejecución. En este ejercicio, Python permite implementar la solución de manera rápida y eficiente para casos pequeños, pero su rendimiento decrece en sistemas más complejos.

### Java

Java es un lenguaje robusto y eficiente, especialmente en aplicaciones de larga duración y procesamiento intensivo. Su tipado estático y la optimización JIT de la JVM garantizan un rendimiento sólido y una detección temprana de errores. Aunque su sintaxis es más verbosa, esto se compensa con herramientas maduras y un ecosistema empresarial consolidado. En este ejercicio, Java ofrece un equilibrio entre rendimiento y escalabilidad, siendo ideal para sistemas más grandes.

### Scala

Scala combina paradigmas funcionales y orientados a objetos, ofreciendo una sintaxis más concisa que Java. Su soporte para inmutabilidad y abstracciones funcionales lo hacen ideal para aplicaciones distribuidas y seguras. Sin embargo, su curva de aprendizaje es más pronunciada, y las abstracciones funcionales pueden introducir sobrecarga. En este ejercicio, Scala es una opción potente para quienes buscan aprovechar la programación funcional.

---

## Resultados de rendimiento

### Python

El tiempo de ejecución en Python es moderado, con una complejidad algorítmica de O(k × m), donde:

- k: número de ingredientes por receta.
- m: tamaño del inventario.

![Tiempo de ejecución de Python](https://i.gyazo.com/fe063ea0c22f5a90009e7ff843cc9872.png)

### Java

Java presenta un tiempo de ejecución eficiente, con una complejidad algorítmica de O(n × m), donde:

- n: número de ingredientes en la receta del día.
- m: número de ingredientes en el inventario.

![Tiempo de ejecución de Java](https://i.gyazo.com/3f10890ab4c66b3140cb44bac756c1b3.png)

### Scala

Scala tiene un rendimiento similar al de Java, con una complejidad algorítmica de O(n × m). Aunque su tiempo de ejecución es competitivo, las abstracciones funcionales pueden añadir ligeras penalizaciones.

![Tiempo de ejecución en Scala](https://i.gyazo.com/9b2f5f840b6a8bcd4420b254210aeb90.png)

---

## Comparación de seguridad

| **Aspecto**                             | **Java**               | **Scala**                     | **Python**                      |
| --------------------------------------- | ---------------------- | ----------------------------- | ------------------------------- |
| **Tipado**                              | Estático               | Estático (más expresivo)      | Dinámico                        |
| **Detección de errores en compilación** | Sí (sólido)            | Sí (más potente)              | No, solo en tiempo de ejecución |
| **Gestión de memoria**                  | Automática (JVM)       | Automática (JVM)              | Automática (CPython)            |
| **Soporte para inmutabilidad**          | Parcial (con esfuerzo) | Alto (programación funcional) | Bajo por defecto                |
| **Riesgo de null-pointer**              | Medio (usa `Optional`) | Bajo (usa `Option`)           | Alto (`None` es común)          |
| **Madurez del ecosistema de seguridad** | Muy alto               | Medio-alto                    | Medio                           |

---

### 1. Modelo de seguridad robusto en la JVM

- Java se ejecuta en la **Máquina Virtual de Java (JVM)**, que implementa un **sandbox de seguridad**.
- Cuenta con un **Security Manager** que puede restringir acceso a archivos, red, procesos, etc.
- Incluye una política de seguridad configurable.

---

### 2. Verificación de bytecode

- El compilador de Java genera bytecode que es **verificado por la JVM antes de su ejecución**.
- Esto evita:
  - Desbordamientos
  - Instrucciones ilegales
  - Errores de acceso a memoria

---

### 3. Tipado estático fuerte

- Java tiene un **sistema de tipos estático y estricto**, lo que permite:
  - Detectar errores en tiempo de compilación
  - Prevenir fallos comunes de tipado dinámico
- Scala también tiene tipado estático, pero más complejo y flexible.

---

### 4. Manejo explícito de permisos y seguridad en bibliotecas

- Java posee un ecosistema maduro y controlado de bibliotecas.
- APIs como `java.security` permiten criptografía, firmas digitales y autenticación (JAAS).

---

### 5. Actualizaciones frecuentes de seguridad

- Java recibe **actualizaciones de seguridad regulares** con amplio soporte comunitario y empresarial.

---

**Java** es más seguro por:

- Su entorno controlado (JVM)
- Tipado fuerte y validación previa a ejecución
- Madurez en prácticas de seguridad
- Infraestructura robusta para control y auditoría del código

## Conclusión

En este ejercicio, **Java** se posiciona como el mejor lenguaje debido a su equilibrio entre rendimiento, escalabilidad y robustez. Aunque Python es ideal para prototipos rápidos y Scala ofrece ventajas en programación funcional, Java sobresale en términos de seguridad, madurez del ecosistema y eficiencia en aplicaciones empresariales. Por lo tanto, es la opción más adecuada para implementar un sistema como el Planificador Funcional de Compras Semanales.
