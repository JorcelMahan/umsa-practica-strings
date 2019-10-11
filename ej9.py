# De una cadena dada, formar una nueva con las posiciones pares que sean la letra 'u' o por las posiciones multiplos de 5

def es_mulitplo_de_5(num):
    return num % 5 == 0


cadena = input('Introduce una cadena: ')
nueva_cadena = ''
for i in range(1, len(cadena)):
    if (i % 2 == 0 and cadena[i] == 'u') or es_mulitplo_de_5(i):
        nueva_cadena += cadena[i]

print(f'Nueva cadena: {nueva_cadena}')