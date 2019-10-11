# Generalizar el ejercicio anterior para cualquie letra

frase_tautograma_c = input('Introduce una frase con tautograma: ')
letra_a_buscar = input('Introduce la letra a buscar: ')
contar_letra = 0
for i in range(len(frase_tautograma_c)):
    if frase_tautograma_c[i] == letra_a_buscar:
        contar_letra += 1
print(f'Cantidad de letras c = {contar_letra}')
