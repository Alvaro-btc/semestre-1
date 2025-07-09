# Ejercicio 2

numero = 500
suma = 0
diferencia = 44
signo = -1 

while numero <= 800:
    suma += numero
    diferencia += 10
    signo *= -1
    numero += signo * diferencia

print("\nLa suma total es:", suma)