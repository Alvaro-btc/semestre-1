entero = int(input('Ingrese un número entero: '))
flotante = float(input('Ingrese un número flotante: '))
complejo = complex(input('ingrese un número complejo: '))

potencia_compleja = (entero ** complejo)
suma_mixta = (complejo + flotante)
producto_mixto = (complejo * entero)
módulo_potencia_compleja = abs(potencia_compleja)

print(potencia_compleja)
print(suma_mixta)
print(producto_mixto)
print(módulo_potencia_compleja)

