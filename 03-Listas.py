#LISTA COMPUESTA DE DATOS
lista1 = ['Álvaro', 19, True]
print(lista1)

#LISTA VACIA
frutas = {}

#LISTA DE SOLO NÚMEROS
n = [1,2,3,4,5]

#LISTA DE SOLO STRINGS
ramos = ['Programación', 'Química', 'POO', 'Proframacion']

#IMPRIME LA POSICIÓN DEL PRIMER ELEMENTO DE LA LISTA (NO EL CARÁCTER)
print(ramos[0])

#FUNCIÓN COUNT ( CUENTA LA CANTIDAD DE CONCURRENCIAS DE UN ELEMENTO)
print(ramos.count('Programación'))

#ELIMINANDO UN ELEMENTO DE LA LISTA
ramos.pop()
print(ramos)

#ORDENANDO ELEMENTOS SEGÚN SU CANTIDAD DE CARACTERES
ramos.sort(key=len)
print(ramos)

#OCUPANDO EL MÉTODO EXTEND (EXTENDIENDO UNA LISTA A PARTIR DE OTRA)
ramos.extend(n)
print(ramos)







