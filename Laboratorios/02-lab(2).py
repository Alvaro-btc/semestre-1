resumen = input("Ingrese el resumen del paper científico: ")

es_resumen_valido = len(resumen) <= 50
print("\n¿El resumen tiene 50 caracteres o menos?")
print(es_resumen_valido)

print("\n--- Análisis del Resumen ---")
print(f"Longitud total: {len(resumen)} caracteres")


print(f"Resumen en mayúsculas: {resumen.upper()}")


print(f"Resumen en minúsculas: {resumen.lower()}")


cantidad_e = resumen.lower().count("e")
print(f"Número de veces que aparece la vocal 'e': {cantidad_e}")


primeros_15 = resumen[:15]
ultimos_15 = resumen[-15:]
print(f"Primeros 15 caracteres: {primeros_15}")
print(f"Últimos 15 caracteres: {ultimos_15}")


resumen_con_comas = ",".join(resumen.split())
print(f"Resumen con palabras separadas por comas: {resumen_con_comas}")











