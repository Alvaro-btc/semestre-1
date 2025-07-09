print('===== Letra A =====')
gatitos = {
    101 : {'nombre' : 'Luna', 'peso' : 1.2,'edad' : 3,'tamaño' : 30},
    102 : {'nombre' : 'Michi', 'peso' : 0.8, 'edad' : 2, 'tamaño' : 25},
    103 : {'nombre' : 'Pepito', 'peso' : 2.5, 'edad' : 5, 'tamaño' : 35}
}

print(gatitos)

print('\n===== Letra B =====')
for ingreso in gatitos:
    peso = gatitos[ingreso]["peso"]

    if peso < 1:
        clasificacion = "Bajo Peso"
    elif peso <= 4:
        clasificacion = "Normal"
    else:
        clasificacion = "Sobre Peso"
    gatitos[ingreso]["Clasificación-Peso"] = clasificacion


for ingreso, datos in gatitos.items():
    print(f"Ingreso {ingreso}: {datos}")



print('\n===== Letra C =====')
for ingreso in gatitos:
    try:
        edad = gatitos[ingreso]["edad"]

        if edad < 4:
            categoria = "Cachorro"
        elif edad <= 12:
            categoria = "Joven"
        else:
            categoria = "Adulto"

    except:
        categoria = "Desconocida"

    gatitos[ingreso]["Categoría-Etaria"] = categoria



for ingreso, datos in gatitos.items():
    print(f"Ingreso {ingreso}: {datos}")




print('\n===== Letra D =====')
lista_pesos = [(ingreso, datos["peso"]) for ingreso, datos in gatitos.items()]

def obtener_peso(tupla):
    return tupla[1]

lista_pesos_ordenada = sorted(lista_pesos, key=obtener_peso)

print("Lista de gatitos ordenada por peso:")
for ingreso, peso in lista_pesos_ordenada:
    print(f"Ingreso {ingreso} - Peso: {peso} kg")


print('\n===== Letra E =====')
while True:
    print("\n--- Ingreso de nuevo gatito ---")

    try:
        ingreso = int(input("Número de ingreso: "))
        nombre = input("Nombre: ")
        peso = float(input("Peso (kg): "))
        edad = int(input("Edad (meses): "))
        tamaño = int(input("Tamaño (cm): "))

        nuevo_gato = {
            "Nombre": nombre,
            "Peso": peso,
            "Edad": edad,
            "Tamaño": tamaño
        }

        gatitos[ingreso] = nuevo_gato

        print(f"Gatito '{nombre}' agregado con éxito.")

    except ValueError:
        print("⚠️ Error: Asegúrate de ingresar números válidos para ingreso, peso, edad y tamaño.")
        continue 

    continuar = input("¿Desea agregar otro gatito? (s/n): ").lower()
    if continuar != "s":
        break


print('\n===== Letra F =====')
print("\n--- Actualizar tamaño de un gatito ---")

try:
    ingreso = int(input("Ingrese el número de ingreso del gatito: "))

    if ingreso in gatitos:
        nuevo_tamaño = int(input("Ingrese el nuevo tamaño (cm): "))
        gatitos[ingreso]["tamaño"] = nuevo_tamaño
        print(f"Tamaño actualizado correctamente para el gatito {gatitos[ingreso]['nombre']}.")
    else:
        print("No se encontró un gatito con ese número de ingreso.")

except ValueError:
    print("Error: Debes ingresar un número válido.")


print('\n===== Letra G =====')
lista = [1.2, 0.8, 2.5]
suma_pesos = sum(lista)
promedio_pesos = (suma_pesos / 3)
print('=== Promedio ===')
print(promedio_pesos)

max_peso = max(lista)
min_peso = min(lista)
print('=== Peso máximo ===')
print(max_peso)
print('=== Peso mínimo ===')
print(min_peso)
