def es_heterograma(cadena):
    """
    Esta función verifica si una cadena es un heterograma, 
    lo que significa que no contiene letras repetidas.
    """
    # Convertir la cadena a minúsculas para evitar distinción entre mayúsculas y minúsculas
    cadena = cadena.lower()
    
    # Usar un conjunto para realizar un seguimiento de las letras ya vistas
    letras_vistas = set()
    
    for letra in cadena:
        # Si la letra ya se ha visto, no es un heterograma
        if letra in letras_vistas:
            return False
        # Agregar la letra al conjunto de letras vistas
        letras_vistas.add(letra)
    
    # Si todas las letras son únicas, es un heterograma
    return True

def es_isograma(cadena):
    """
    Esta función verifica si una cadena es un isograma, lo que significa que no 
    contiene letras repetidas,
    considerando tanto mayúsculas como minúsculas como iguales.
    """
    # Convertir la cadena a minúsculas para evitar distinción entre mayúsculas y minúsculas
    cadena = cadena.lower()
    
    # Usar un conjunto para realizar un seguimiento de las letras ya vistas
    letras_vistas = set()
    
    for letra in cadena:
        # Si la letra ya se ha visto, no es un isograma
        if letra in letras_vistas:
            return False
        # Agregar la letra al conjunto de letras vistas
        letras_vistas.add(letra)
    
    # Si todas las letras son únicas, es un isograma
    return True

def es_pangrama(cadena):
    """
    Esta función verifica si una cadena es un pangrama, lo que significa 
    que contiene todas las letras del alfabeto.
    """
    # Convertir la cadena a minúsculas para evitar distinción entre mayúsculas y minúsculas
    cadena = cadena.lower()
    
    # Usar un conjunto para realizar un seguimiento de las letras del alfabeto
    letras_del_alfabeto = set('abcdefghijklmnopqrstuvwxyz')
    
    for letra in cadena:
        # Si la letra es una letra del alfabeto, eliminarla del conjunto
        if letra in letras_del_alfabeto:
            letras_del_alfabeto.remove(letra)
    
    # Si el conjunto de letras del alfabeto está vacío, es un pangrama
    return not letras_del_alfabeto

# Ejemplo de uso:
cadena = input("Introduce un texto, puede ser una palabra u oracion: ")
if es_pangrama(cadena):
    print(f"El texto {cadena} Es un pangrama.")
elif es_heterograma(cadena):
    print(f"El texto {cadena} Es un heterograma.")
elif es_isograma(cadena):
    print(f"El texto {cadena} Es un isograma.")
else:
    print(f"El texto {cadena} No es ninguno de los tres.")