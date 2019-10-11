# Dado una frase con tautograma contar cuantas vocales tiene
def es_vocal(letra):
    return letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' or letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U'


frase_tautograma = input("Introduce una frase con tautograma: ")
cantidad_vocales = 0;
for i in range(len(frase_tautograma)):
    if es_vocal(frase_tautograma[i]):
        cantidad_vocales += 1

print(f'Cantidad de vocales = {cantidad_vocales}')
