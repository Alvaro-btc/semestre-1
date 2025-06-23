





mes = 4
match mes:
    case 12 | 1 | 2:
        print("Verano")
    case 3 | 4 | 5:
        print("Otoño")
    case 6 | 7 | 8:
        print("Invierno")
    case 9 | 10 | 11:
        print("Primavera")
    case _:
        print("Mes inválido")









#PATRONES COMPUESTOS
x = [1, 2, 3]
match x:
    case [a, b, c]:  #DESAGRUPANDO VALORES DE LA LISTA X
        print(f"Elementos de la lista x: {a}, {b}, {c}")








