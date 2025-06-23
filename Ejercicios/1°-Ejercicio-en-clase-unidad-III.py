#Ejercicio 1 en clases, unidad III
productos = ['Smartphone', 'Laptop', 'Tablet', 'Smartwatch']
valores = [300, 800, 150, 200]
stock = {
    'Smartphone': 25,
    'Laptop': 12,
    'Tablet': 8,
    'Smartwatch': 4
}

#Min-Max
max_precio = max(valores)
min_precio = min(valores)

#Nombre productos más caro y más barato
prod_max = productos[valores.index(max_precio)]
prod_min = productos[valores.index(min_precio)]

print(f'El articulo más caro es {prod_max} con un valor de {max_precio}')
print(f'El articulo más barato es {prod_min} con un valor de {min_precio}\n\n')

#Categorias
for prod, precio in zip(productos, valores):
    if precio < 200:
        categoria = 'Producto Económico'
    elif precio <= 200 and precio <= 500:
        categoria = 'Producto Estándar'
    else:
        categoria = 'Producto Premium'
    print(f'{prod}: ${precio} -> {categoria}')

#Stock
for prod, cantidad in stock.items():
    if cantidad < 10:
        print(f'{prod}: {cantidad} unidades')