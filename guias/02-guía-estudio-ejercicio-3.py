# Ejercicio 3
ventas = {
    'Marco': [350000, 200000, 180000, 150000, 190000],
    'Álvaro': [400000, 380000, 420000, 390000, 410000],
    'Lia': [160000, 170000, 150000, 180000, 140000]
}

sueldo_base = 529000

def calcular_bono(total_ventas):
    if total_ventas > 1_500_000:
        return 0.20 * sueldo_base
    elif total_ventas > 1_000_000:
        return 0.10 * sueldo_base
    elif total_ventas > 500_000:
        return 0.05 * sueldo_base
    else:
        return 0


print("REPORTE DE SUELDOS Y BONOS\n")
for vendedor, ventas_diarias in ventas.items():
    total_semanal = sum(ventas_diarias)
    bono = calcular_bono(total_semanal)
    promedio = total_semanal / len(ventas_diarias)
    sueldo_total = sueldo_base + bono
    
    print(f"Vendedor: {vendedor}")
    print(f"  Ventas semanales: ${total_semanal:,}")
    print(f"  Bono: ${bono:,.0f}")
    print(f"  Promedio diario de ventas: ${promedio:,.0f}")
    print(f"  Sueldo total a pagar: ${sueldo_total:,.0f}")
    print("-" * 40)


