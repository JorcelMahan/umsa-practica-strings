# Insertar un caracter nuevo cada 5 caracteres de la cadena

cadena = input('Insertar una cadena: ')
caracter = input('Insertar un caracter: ')
nueva_palabra = [];
for i in range(0, len(cadena)):
    if (i % 5 == 0 and i != 0):
        nueva_palabra.append(caracter)
    nueva_palabra.append(cadena[i])
print(''.join(nueva_palabra))
