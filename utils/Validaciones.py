import math

# metodo para validar los nombres y apellidos
def solo_alpha_spaces(cadena):
    corecta = True
    i = 0
    while corecta and i < len(cadena):
        subcadena = cadena[i:i + 1]
        if not (subcadena.isalpha()) and not (subcadena.isspace()):
            corecta = False
        i += 1
    if corecta:
        if len(cadena) < 3:
            corecta = False

    return corecta


def reducir_a_cifras_significativas(numero, cifras):
    posiciones = pow(10.0, cifras)
    return math.trunc(posiciones*numero)/posiciones

