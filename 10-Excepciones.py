entrada = input('Ingrese un valor entero:')

try:
    numero = int(entrada)
    print(f'Número ingresado: {numero}')
except ValueError: # Error por tipo de dato
    print('Error de valor: el valor ingresado no es entero')
except Exception as e: # Errores genericos e inesperados
    print('Error inesperado: {e}')
else:
    print('Conversión exitosa')
finally:
    print('Finalización exitosa\n')


x = 10
y = 0
try:
    resultado = x / y
except ZeroDivisionError:
    print('No se puede dividir por cero')
else:
    print(f'Resultado: {resultado}')
finally:
    print('Operación de división completa')


#Raise
edad = -3
if edad < 0:
    raise ValueError('La edad no puede ser negativa')



