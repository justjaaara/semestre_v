# Reto de Programación Funcional en Scala

## Integrantes:

- Felipe Villa Jaramillo
- Juan Pablo Cardona Bedoya
- Luis Pablo Goez

## Descripción del Reto

Este reto consiste en desarrollar un sistema de análisis de ventas de vehículos utilizando programación funcional en Scala. El proyecto debe implementar distintas operaciones de manipulación de datos utilizando métodos funcionales.

## Objetivos

- [x] Calcular el total de ventas por marca usando groupBy y map.
- [x] Filtrar vehículos vendidos con precio mayor a 30 M (COP) usando filter.
- [ ] Encontrar el vehículo más caro vendido usando reduce en el último año vigente.
- [ ] Ordenar las ventas por año del vehículo de más reciente a más antiguo usando sortBy.
- [ ] Generar un reporte en formato JSON con las estadísticas generadas.

## Restricciones de Código

- **No usar bucles tradicionales** (for, while), solo métodos funcionales.
- El código debe ser organizado con funciones reutilizables.
- No incluir comentarios innecesarios para la sustentación.

## Clases Principales

### Vehiculo

Representa un vehículo con los siguientes atributos:

- ID
- Marca
- Modelo
- Año
- Precio

### Venta

Representa una transacción de venta con:

- ID de venta
- Vehículo vendido
- Comprador
- Vendedor

## Funcionalidades a Implementar

### 1. Total de Ventas por Marca

Calcular el total de ventas por cada marca de vehículo utilizando las funciones `groupBy` y `map`.

### 2. Filtrado de Vehículos Caros

Filtrar los vehículos con precio superior a 30 millones de pesos utilizando la función `filter`.

### 3. Vehículo Más Caro del Último Año

Encontrar el vehículo más caro vendido en el último año utilizando la función `reduce`.

### 4. Ordenamiento de Ventas por Año

Ordenar las ventas de vehículos del más reciente al más antiguo utilizando la función `sortBy`.

### 5. Generación de Reporte JSON

Generar un reporte en formato JSON con todas las estadísticas calculadas.

---

Este proyecto forma parte del curso de Lenguajes y Paradigmas de Programación.
