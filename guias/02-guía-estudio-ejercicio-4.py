# Ejercicio 4
n = int(input("\nIngrese el valor de n: "))
impar = 1

for i in range(1, n + 1):
    suma = 0
    conteo = 0
    while conteo < i:
        suma += impar
        impar += 2
        conteo += 1
    print(f"{i}³ = {suma}\n")