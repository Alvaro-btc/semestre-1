# Martillo
precio_martillo = float(input("Ingrese el precio unitario del martillo: "))
cantidad_martillo = int(input("Ingrese la cantidad de martillos: "))

# Clavos
precio_clavos = float(input("Ingrese el precio unitario de los clavos: "))
cantidad_clavos = int(input("Ingrese la cantidad de clavos: "))

# Serrucho
precio_serrucho = float(input("Ingrese el precio unitario del serrucho: "))
cantidad_serrucho = int(input("Ingrese la cantidad de serruchos: "))

# Tornillos
precio_tornillos = float(input("Ingrese el precio unitario de los tornillos: "))
cantidad_tornillos = int(input("Ingrese la cantidad de tornillos: "))

subtotal_martillo = round(precio_martillo * cantidad_martillo, 2)
subtotal_clavos = round(precio_clavos * cantidad_clavos, 2)
subtotal_serrucho = round(precio_serrucho * cantidad_serrucho, 2)
subtotal_tornillos = round(precio_tornillos * cantidad_tornillos, 2)

def formato_pesos(valor):
    return "$" + format(valor, ",.2f").replace(",", "X").replace(".", ",").replace("X", ".")

print("\n--- Subtotales en Pesos Chilenos ---")
print(f"Subtotal Martillo: {formato_pesos(subtotal_martillo)}")
print(f"Subtotal Clavos: {formato_pesos(subtotal_clavos)}")
print(f"Subtotal Serrucho: {formato_pesos(subtotal_serrucho)}")
print(f"Subtotal Tornillos: {formato_pesos(subtotal_tornillos)}")

total = subtotal_martillo + subtotal_clavos + subtotal_serrucho + subtotal_tornillos

valor_maximo = max(subtotal_martillo, subtotal_clavos, subtotal_serrucho, subtotal_tornillos)
valor_minimo = min(subtotal_martillo, subtotal_clavos, subtotal_serrucho, subtotal_tornillos)

promedio_precios = round((precio_martillo + precio_clavos + precio_serrucho + precio_tornillos) / 4, 2)

iva = round(total * 0.19, 2)

print("\n--- Resultados Finales en Pesos Chilenos ---")
print(f"Suma total: {formato_pesos(total)}")
print(f"Valor máximo entre subtotales: {formato_pesos(valor_maximo)}")
print(f"Valor mínimo entre subtotales: {formato_pesos(valor_minimo)}")
print(f"Promedio del precio unitario: {formato_pesos(promedio_precios)}")
print(f"IVA (19%) del total: {formato_pesos(iva)}")

