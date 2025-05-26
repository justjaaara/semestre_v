'''
1. Reciba un menú semanal (lista de recetas por día). 
2. Verifique los ingredientes disponibles en inventario. 
3. Calcule la lista de compras con cantidades agregadas de lo que falta. 
4. Opcional: clasifique los productos por categoría (e.g., frutas, carnes, lácteos). 
'''
import time

INVENTARIO = [{'nombre': 'tomate', 'cantidad': 1, 'unidad': 'pieza'},
              {'nombre': 'pasta', 'cantidad': 100, 'unidad': 'gramos'}]

MENU_SEMANAL = {
    "lunes": {
        "receta": "ensalada",
        "ingredientes": [{"nombre": "lechuga", "cantidad": 1, "unidad": "pieza"},
                        {"nombre": "tomate", "cantidad": 2, "unidad": "pieza"}]
    },
    "martes": {
        "receta": "pasta",
        "ingredientes": [{"nombre": "pasta", "cantidad": 200, "unidad": "gramos"},
                        {"nombre": "papas", "cantidad": 1, "unidad": "pieza"}]
    },
    "miércoles": {
        "receta": "frijoles",
        "ingredientes": [{"nombre": "frijol", "cantidad": 100, "unidad": "gramos"},
                        {"nombre": "cebolla", "cantidad": 1, "unidad": "pieza"},
                        {"nombre": "platano", "cantidad": 1, "unidad": "pieza"}]
    },
    "jueves": {
        "receta": "sopa",
        "ingredientes": [{"nombre": "pasta", "cantidad": 100, "unidad": "gramos"},
                        {"nombre": "tomate", "cantidad": 1, "unidad": "pieza"},
                        {"nombre": "cebolla", "cantidad": 1, "unidad": "pieza"}]
    },
    "viernes": {
        "receta": "tacos",
        "ingredientes": [{"nombre": "tortilla", "cantidad": 2, "unidad": "pieza"},
                        {"nombre": "carne", "cantidad": 200, "unidad": "gramos"},
                        {"nombre": "tomate", "cantidad": 1, "unidad": "pieza"},
                        {"nombre": "cebolla", "cantidad": 1, "unidad": "pieza"}]
    },
    "sábado": {
        "receta": "pizza",
        "ingredientes": [{"nombre": "masa", "cantidad": 1, "unidad": "pieza"},
                        {"nombre": "tomate", "cantidad": 2, "unidad": "pieza"},
                        {"nombre": "queso", "cantidad": 100, "unidad": "gramos"}]
    },
    "domingo": {
        "receta": "ensalada",
                    "ingredientes": [{"nombre": "lechuga", "cantidad": 1, "unidad": "pieza"},
                                      {"nombre": "tomate", "cantidad": 2, "unidad": "pieza"}]}}

def recibir_menu_semanal():
    start_time = time.time()
    
    dia_seamna = input("Ingrese el día de la semana: ")
    verificar_inventario(dia_seamna)
    
    end_time = time.time()
    print("\nTiempo total de ejecución: {:.6f} segundos".format(end_time - start_time))

def verificar_cantidad_ingrediente(ingredientes):
    start_time = time.time()
    
    ingredientes_faltantes = []

    for ingrediente in ingredientes:
        if ingrediente[0] not in [item['nombre'] for item in INVENTARIO]:
            ingredientes_faltantes.append(ingrediente)
        else:
            item = next((item for item in INVENTARIO if item['nombre'] == ingrediente[0]), None)
            ingredientes_faltantes.append([ingrediente[0], ingrediente[1] - item["cantidad"], ingrediente[2]])
    
    end_time = time.time()
    print("\nTiempo de verificación de ingredientes: {:.6f} segundos".format(end_time - start_time))
    
    return ingredientes_faltantes

def verificar_inventario(dia_semana):
    start_time = time.time()
    
    receta_a_verificar = MENU_SEMANAL[dia_semana]

    ingredientes_dia = map(lambda x: [x['nombre'], x['cantidad'], x['unidad']], receta_a_verificar['ingredientes'])
    ingredientes_dia = list(ingredientes_dia)
    ingredientes_faltantes = verificar_cantidad_ingrediente(ingredientes_dia)
    print("INGREDIENTES DEL DÍA", list(ingredientes_dia))
    print("INGREDIENTES FALTANTES", list(ingredientes_faltantes))
    
    end_time = time.time()
    print("\nTiempo de verificación de inventario: {:.6f} segundos".format(end_time - start_time))

# Medición de tiempo total
start_time_total = time.time()
recibir_menu_semanal()
end_time_total = time.time()
print("\nTiempo total del programa: {:.6f} segundos".format(end_time_total - start_time_total))