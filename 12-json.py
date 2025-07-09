import json # Manipulación de archivos json
import os   #Métodos para trabajar con el SO

ruta = os.path.join("json", "datos.json") # Ruta relativa --> json/datos.json

# Leer el archivo json
print("==== LECTURA DEL JSON ====")
#utf-8 es el encoding para trabajar idioma español
# La letra r es de read = lectura
with open(ruta, "r", encoding='utf-8') as archivo: 
    datos =json.load(archivo) # Conversión de JSON a estructura de python

# Mostrar los usuarios del archivo JSON
for usuario in datos:
    print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Edad: {usuario['edad']}")

# Escritura de archivo JSON
print("==== ESCRITURA DEL JSON ====")

# Agregar un nuevo usuario
nuevo_usuario = {
    "id": 5,
    "nombre": "Fernanda",
    "edad": 30
}

datos.append(nuevo_usuario)

# Guardar los cambios en el archivo JSON utilizando json.dump()
# w = write = escribir

with open(ruta, "w", encoding='utf-8') as archivo:
    json.dump(
        datos,
        archivo,
        indent=4
    )