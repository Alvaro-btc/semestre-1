# Ejercicio 7
def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
        return n * factorial(n - 1)
    else:
        raise ValueError("El número debe ser un entero no un negativo")
    
numero = int(input("Ingresa un número entero no negativo: "))
print(f"\nEl factorial de {numero} es: {factorial(numero)}\n")