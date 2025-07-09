# A. Diccionario Principal
clima = {
    5700000: {
        "Ciudad": "Castro",
        "Temperatura": 11.8,
        "Precipitación": 2000
    },
    5770000: {
        "Ciudad": "Chonchi",
        "Temperatura": 8.3,
        "Precipitación": 2800
    },
    5790000: {
        "Ciudad": "Quellón",
        "Temperatura": 10.2,
        "Precipitación": 2950
    }
}

print("========= A. DICCIONARIO INICIAL =========")
print(clima)


# B. Se agrega la nueva clave "Clima" a los sub-diccionarios, usando condicionales y try-except
print("\n========= B. TIPO DE CLIMA =========")

# Castro
try:
    temp_castro = clima[5700000]["Temperatura"]
    if temp_castro < 10:
        clima[5700000]["Clima"] = "Frío"
    elif temp_castro <= 15:
        clima[5700000]["Clima"] = "Templado"
    else:
        clima[5700000]["Clima"] = "Cálido"
except:
    clima[5700000]["Clima"] = "Desconocida"

# Chonchi
try:
    temp_chonchi = clima[5770000]["Temperatura"]
    if temp_chonchi < 10:
        clima[5770000]["Clima"] = "Frío"
    elif temp_chonchi <= 15:
        clima[5770000]["Clima"] = "Templado"
    else:
        clima[5770000]["Clima"] = "Cálido"
except:
    clima[5770000]["Clima"] = "Desconocida"

# Quellón
try:
    temp_quellon = clima[5790000]["Temperatura"]
    if temp_quellon < 10:
        clima[5790000]["Clima"] = "Frío"
    elif temp_quellon <= 15:
        clima[5790000]["Clima"] = "Templado"
    else:
        clima[5790000]["Clima"] = "Cálido"
except:
    clima[5790000]["Clima"] = "Desconocida"
    
print(clima)  
    

# C. Lista vacía "MesesLluviosos". Se agrega meses con append() y eliminar "Junio" con pop()
print("\n========= C. MESES LLUVIOSOS =========")
clima[5700000]["MesesLluviosos"] = []
clima[5700000]["MesesLluviosos"].append("Mayo")
clima[5700000]["MesesLluviosos"].append("Junio")
clima[5700000]["MesesLluviosos"].append("Julio")
clima[5700000]["MesesLluviosos"].pop(1)  

print(clima)  

# D. Actualizando nombre de ciudad Chonchi
print("\n========= D. NUEVO NOMBRE CHONCHI =========")
clima[5770000]["Ciudad"] = clima[5770000]["Ciudad"].replace("Chonchi", "Ciudad de los Tres Pisos") # también sirve update()

# E. Nueva lista de lluvias (suma, máximo, mínimo, índice del mayor valor)
lluvias = [clima[5700000]["Precipitación"], clima[5770000]["Precipitación"], clima[5790000]["Precipitación"]]
print(clima)

print("\n========= E. ANÁLISIS DE PRECIPITACIONES =========")
print("Suma total de precipitaciones:", sum(lluvias))
print("Mayor precipitación:", max(lluvias))
print("Menor precipitación:", min(lluvias))
print("Índice de la precipitación más alta:", lluvias.index(max(lluvias)))

# F. Diccionario completo con todos los cambios
print("\n========= F. DICCIONARIO ACTUALIZADO =========")
print(clima)

# G. Lista de tuplas con claves y valores
tuplas = list(clima.items())
print("\n========= G. LISTA DE TUPLAS (CLAVE, VALOR) =========")
print(tuplas)
