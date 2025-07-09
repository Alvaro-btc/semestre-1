numeros = list(range(500, 99, -3))
for n in numeros:
    print(n)

suma_total = sum(numeros)
promedio = suma_total / len(numeros)

print(f"\nSuma total: {suma_total}")
print(f"Promedio: {promedio:.2f}")
