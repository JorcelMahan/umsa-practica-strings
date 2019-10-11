# Dada una frase contar cuantas palabras son capicuas
def es_capicua(plb):
    aux = list(plb)
    aux.reverse()
    plb_reverse = "".join(aux)
    return plb == plb_reverse

frase = input('Introduce una frase: ')
arr_frase = frase.split()
cantidad_capicuas = 0
for plb in arr_frase:
    if es_capicua(plb):
        cantidad_capicuas += 1

print(f'La cantidad de capicuas es = {cantidad_capicuas}')