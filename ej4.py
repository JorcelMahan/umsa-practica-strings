# Convertir todas las letras minusculas a mayuscula e invertirla

cadena = input('Introduce una cadena: ')
nueva_cadena = ''
# list_ascii = [ord(c) for c in cadena]
for i in range(0, len(cadena)):
    value = cadena[i]
    if(ord(cadena[i]) >= 97 and ord(cadena[i]) <=122):
        value = cadena[i].upper()
    if(ord(cadena[i]) >= 65 and ord(cadena[i]) <=90):
        value = cadena[i].lower()
    nueva_cadena += value
print(nueva_cadena)