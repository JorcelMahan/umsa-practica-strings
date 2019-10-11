# Verificar si una palabra es ciclograma
def construir_palabra(arr, palabra):
    j = 0
    plb = ''
    while j < len(arr):
        plb += palabra[arr[j]]
        j += 1
    return plb


palabra = input('Introduce una palabra: ')
ultimo_caracter = palabra[-1]
i = palabra.find(ultimo_caracter) + 1
if palabra.count(palabra[i - 1]) > 1:
    a = [x for x in range(0, i)]
    b = [x for x in range(len(palabra) - 1, len(palabra) - 1 - len(a), -1)]
    b.reverse()
    if construir_palabra(a, palabra) == construir_palabra(b, palabra):
        print(f'La palabra {palabra} es ciclograma')
    else:
        print(f'La palabra {palabra} no es ciclograma')

else:
    print(f'La palabra {palabra} no es ciclograma')
