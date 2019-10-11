# Dada una frase con puntuacion, eliminar todas las puntuaciones y cambiarlas por espacios y mostra la frase
frase = input('Introduce una frase: ')
frase = frase.replace(',', ' ')
frase = frase.replace('.', ' ')

print(frase)
