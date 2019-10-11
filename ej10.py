# De una cadena dada, formar una nueva con las letras 'f'. 'i', o con las posiciones que sean numeros primo
def es_primo(number):
    if number == 0:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


cadena = input('Introduce una cadena: ')
nueva_cadena = ''
for i in range(len(cadena)):
    if cadena[i] == 'i' or cadena[i] == 'f' or es_primo(i):
        nueva_cadena += cadena[i]

print(f'Nueva cadena: {nueva_cadena}')
