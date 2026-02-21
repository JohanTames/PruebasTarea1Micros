def filtrar_vocales(cadena, bandera):
    if not isinstance(cadena, str):
        return -100, None

    # Primero que isalpha() porque sino devuelve -200 si cadena está vacío
    if cadena == "":
        return -300, None

    if not cadena.isalpha():
        return -200, None

    if len(cadena) > 30:
        return -400, None

    if not isinstance(bandera, bool):
        return -500, None

    vocales = "aeiouAEIOU"

    resultado = ""

    if bandera:
        for c in cadena:
            if c in vocales:
                resultado += c
    else:
        for c in cadena:
            if c not in vocales:
                resultado += c

    return 0, resultado


def encontrar_extremos(lista_numeros):
    if not isinstance(lista_numeros, list):
        return -600, None, None

    for elemento in lista_numeros:
        # Bool es subclase de int
        if (
            not isinstance(elemento, (int, float))
            or isinstance(elemento, bool)
        ):
            return -700, None, None

    if len(lista_numeros) == 0:
        return -800, None, None

    if len(lista_numeros) > 15:
        return -900, None, None

    minimo = min(lista_numeros)
    maximo = max(lista_numeros)

    return 0, minimo, maximo
