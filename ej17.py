# Dada una frase verificar que es un pleonasmo
import requests
from bs4 import BeautifulSoup

url = 'http://www.wordreference.com/sinonimos/'
enlace = input("palabra a buscar: ")
buscar = url + enlace
resp = requests.get(buscar)
bs = BeautifulSoup(resp.text, 'lxml')
lista = bs.find_all(class_='trans clickable')
for sin in lista:
    sino = sin.find_all('li')
    for fin in sino:
        print(fin.next_element)
