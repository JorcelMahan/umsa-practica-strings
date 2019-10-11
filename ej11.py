# Dada una frase con puntuacion, eliminar las comas y mostrar la frase
frase = input('Introduce una frase: ')
frase_sin_comas = frase.split(',')
frase_sin_comas = "".join(frase_sin_comas)
print(frase_sin_comas)