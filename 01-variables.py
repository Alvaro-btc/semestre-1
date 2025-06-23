nombre = 'Álvaro'
apellido = 'Torres'

# Print con comas
print("Hola mi nombre es:" , nombre, "Y mi apellido es:" , apellido)

# Print con operador de concatenación
print("Hola mi nombre es" + nombre + "y mi apellido es" + apellido)

# Con f-strings (cadenas literales)
print(f"Hola mi nombre es {nombre} y mi apellido es {apellido}")

# Inicalizando multi variables en una sola linea (no recomendable)
ciudad, región, país = "Quellón", "Los Lagos", "Chile"
print(f"Hola soy de {ciudad}, {región}, {país}")