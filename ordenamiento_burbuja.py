import time 
import random

#Generar intervalos
def generar_intervalos(cantidad):
    elementos = [
        max(1, cantidad // 4),
        max(1, cantidad //2),
        cantidad
    ]
    return sorted(set(elementos))

#Generar numeros
def generar_numeros(cantidad):
    inicio = time.perf_counter()
    datos = [random.randint(0, 5_000_000) for _ in range(cantidad)]
    fin = time.perf_counter()
    tiempo = fin - inicio
    return datos, tiempo

cantidad = int(input("Cantidad de elementos"))
datos, tiempo = generar_numeros(cantidad)
print("Iniciar ")
print(f"Tiempo en ejecucion: {tiempo:.4f}")
print("Fin de generacion ")
ini = time.perf_counter()
print(datos)
fin = time.perf_counter()
dif = fin - ini
print(f"Tiempo en ejecucion: {tiempo:.4f}")
print(f"Duracion de impresion {dif:.4f}")

