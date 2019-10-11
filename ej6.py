# Dada una cadena, formar una nueva con las posiciones que sean multiplos de 9 y primos

def es_multiplo_de_9(number):
    return number % 9 == 0


def es_primo(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


cadena = input('Introduce una cadena: ')
nueva_cadena = ''
for i in range(len(cadena)):
    if (es_multiplo_de_9(i) and es_primo(i) and i != 0):
        nueva_cadena += cadena[i]
print('nueva cadena: ', nueva_cadena)
