def obtener_valores_de_parametros(url):
    """
    Esta función toma una URL con parámetros y devuelve una lista de los valores de esos parámetros.
    """
    # Dividir la URL en base al signo de interrogación ('?')
    partes = url.split('?')
    
    # Verificar si hay al menos dos partes (la parte antes del '?' y los parámetros después del '?')
    if len(partes) < 2:
        return []

    # Obtener la parte que contiene los parámetros
    parametros_parte = partes[1]

    # Dividir los parámetros en base al signo '&'
    parametros = parametros_parte.split('&')

    # Crear una lista para almacenar los valores de los parámetros
    valores_parametros = []

    for parametro in parametros:
        # Dividir cada parámetro en base al signo '=' para obtener el nombre y el valor
        nombre, valor = parametro.split('=')
        valores_parametros.append(valor)

    return valores_parametros

# Ejemplo de uso:
url = "https://retosdeprogramacion.com?year=2023&challenge=0&theme=python&option=magic"
valores_parametros = obtener_valores_de_parametros(url)
print(valores_parametros)
