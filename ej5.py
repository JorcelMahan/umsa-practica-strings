# Quitar algunos caracteres de una cadena dada (sin utilizar otra cadena)

cadena = input('Introduce una cadena: ')
caracter = input('Introduce el caracter a eliminar: ')
while (caracter != ''):
    cadena = cadena.replace(caracter, '')
    print(cadena)
    caracter = input('Introduce el caracter a eliminar')
print(cadena)
