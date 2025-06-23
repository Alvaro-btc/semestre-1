num = 0
while num <= 100:
    print(num)
    num += 2


#Continue
print('Forma continue')
n = 0

while n <= 50:
    n += 1
    if n == 40:
        continue
    print(n)


#For
print('Bucle for')

newlista = [1,2,3,4,5,6,7,8,9,10]
for i in newlista:
    print(i)


#Range
print('Función Range')
for i in range(1,10):
    print(i)


#Controles avanzados de bucle

#Ejemplo: Busqueda de número primo
for n in range(1,10):
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} es un número compuesto, divisible por {i}")
            break
    else:
        print(f"{n} es un número primo")



#Matrizes
print("===== MATRIZ 3x3 =====")
matriz = [
    [1, 2, 3], #fila 0
    [4, 5, 6], #fila 1
    [7, 8, 9]  #fila 2
]  #c0 #c1 #c2
for fila_id, fila in enumerate(matriz):
    for col_id, valor in enumerate(fila):
        print(f"Posición ({fila_id},{col_id}) = {valor}")
















