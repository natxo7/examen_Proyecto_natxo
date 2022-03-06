def media(lista_numeros): 
    """Calcula la media de una lista
    Args: lista_numeros (list[])
    Returns: float
    """
    suma = 0
    for n in lista_numeros:
        suma = suma + n
    return suma / len(lista_numeros)

#------------main-------------
num = [1, 5, 3, 2]

resultado = media(num)
print("El resultado es "+str(resultado))
