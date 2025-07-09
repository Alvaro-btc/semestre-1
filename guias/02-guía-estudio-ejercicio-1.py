# Ejercicio 1
import string
try:
    parrafo = input("Ingrese un parrafo: ")
    if not parrafo.strip():
        raise ValueError("El texto no puede estar vacío.")
except ValueError as e:
    print("Error", e)

parrafo_limpio = parrafo.translate(str.maketrans("", "", string.punctuation))

lista_palabras = parrafo_limpio.split()
print(lista_palabras)

palabra_buscada = input("¿Qué palabra quieres buscar (respetando mayúsculas y minúsculas)?: ")
cantidad = lista_palabras.count(palabra_buscada)
print(f"La palabra '\n{palabra_buscada}' aparece {cantidad} veces (distinguiendo mayúsculas).")

