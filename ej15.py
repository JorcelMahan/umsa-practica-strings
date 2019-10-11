# Verificar que una palabra sea adyacente

palabra = input('Introduce una palabra: ')

def es_adyacente(plb):
    for i in range(len(palabra) - 1):
        if palabra[i] != 'l' and palabra[i] != 'r':
            if palabra[i] == palabra[i+1]:
                return True;
    return False

if es_adyacente(palabra):
    print(f'{palabra} es adyacente')
else:
    print(f'{palabra} no es adyacente')
