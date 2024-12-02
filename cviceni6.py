'''
import random

moznosti = ['kamen', 'nuzky', 'papir']
hrac = 'kamen'
pocitac = random.choice(moznosti)

print('Hráč:', hrac)
print('Počítač:', pocitac)

if pocitac == 'kamen':
    print('Nerozhodně')
elif pocitac == 'nuzky':
    print('Vyhrál jsi!')
else:
    print('Prohrál jsi :(')


import os

jmena_slozek = ["obrazky", "texty", "gify"]

while len(jmena_slozek) > 0:
    jmeno_slozky = jmena_slozek.pop()
    if not (os.path.exists(jmeno_slozky) and os.path.isdir(jmeno_slozky)):
        os.mkdir(jmeno_slozky)
        print('Tvořím novou složku:', jmeno_slozky)
    else:
        print('Složka již existuje!')
else:
    print('Všechny složky existují')

'''

import random

min_hodnota = 1
max_hodnota = 6

while True:
    print('Hazim kostkou')
    kostka_hodnota = random.randint(min_hodnota, max_hodnota)
    print('Na kostce je:', kostka_hodnota)
    if kostka_hodnota == 6:
        continue
    else:
        break