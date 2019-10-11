# Dado una frase con tautograma con la letra 'c', mostrar cuantas veces se repita esta letra

frase_tautograma_c = input('Introduce una frase con tautograma con la letra \'c \' : ')
contar_c = 0
for i in range(len(frase_tautograma_c)):
    if frase_tautograma_c[i] == 'c':
        contar_c += 1
print(f'Cantidad de letras c = {contar_c}')
