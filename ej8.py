# Dado n obreos ingresar sus nombres, apellidos, carnet y mostrar en pantalla
def push_obrero(nombre, apellidos, carnet):
    obrero = []
    obrero.append(nombre)
    obrero.append(apellidos)
    obrero.append(carnet)
    obreros.append(obrero)


def show_obrero(obrero):
    for attibuto in obrero:
        print(attibuto, end=" ")


cantidad_obreros = int(input('Introduce la cantidad de obreros: '))
obreros = []
for i in range(cantidad_obreros):
    nombre = input('Introduce nombre: ')
    apellidos = input('Introduce apellidos: ')
    carnet = input('Introduce carnet: ')
    push_obrero(nombre, apellidos, carnet)

for obrero in obreros:
    show_obrero(obrero)
