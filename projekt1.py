"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Filip Tomasch
email: ftukyt@gmail.com
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

from pprint import pprint

cara = '----------------------------------------'
pocet_textu = len(TEXTS)
uzivatele = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

#LOGIN
user = input('username:')
password = input('password:')

if not user in uzivatele.keys():
    print('unregistered user, terminating the program..')
    exit()
elif not uzivatele[user] == password:
    print('wrong password, terminating the program..')
    exit()
else:
    print(cara)
    print('Welcome to the app,', user)
    print(f'We have {pocet_textu} texts to be analyzed.', cara, sep="\n")

#VYBER TEXTU
text_vyber = int(input(f'Enter a number btw. 1 and {pocet_textu} to select: '))

if not text_vyber in range(1, pocet_textu + 1):
    print(f'text number {text_vyber} does not exist, terminating the program..')
    exit()
else:
    print(cara)

#ANALYZA
vycistena_slova = [
    slovo.strip('.,<>?:!')
    for slovo in TEXTS[text_vyber - 1].split()
]

#POCET SLOV
print(f'There are {len(vycistena_slova)} words in the selected text.')

#POCET TITLE SLOV
title = 0
for slovo in vycistena_slova:
    if slovo.istitle():
        title += 1
else:
    print(f'There are {title} titlecase words.')

#POCET UPPER SLOV
upper = 0
for slovo in vycistena_slova:
    if slovo.isalpha() and slovo.isupper():
        upper += 1
else:
    print(f'There are {upper} uppercase words.')

#POCET LOWER SLOV
lower = 0
for slovo in vycistena_slova:
    if slovo.isalpha() and slovo.islower():
        lower += 1
else:
    print(f'There are {lower} lowercase words.')

#POCET CISELNYCH STRINGU
cisel = 0
for slovo in vycistena_slova:
    if slovo.isnumeric():
        cisel += 1
else:
    print(f'There are {cisel} numeric strings.')

#SUMA CISELNYCH STRINGU
suma = 0
for slovo in vycistena_slova:
    if slovo.isnumeric():
        suma += int(slovo)
else:
    print(f'The sum of all the numbers {suma}')

print(cara)


#SERAZENI PODLE POCTU JEDNOTLIVYCH DELEK SLOV
delky_list = [
    len(slovo)
    for slovo in vycistena_slova
]

delky_tuple = tuple(set(delky_list))

pocty = [
    delky_list.count(delka)
    for delka in delky_tuple
]

slovnik_poctu = {
    delky_tuple[_]: pocty[_]
    for _ in range(len(delky_tuple))
}

print('LEN|', 'OCCURENCES'.center(22), '|NR.'.ljust(22), sep='')
print(cara)
for par in slovnik_poctu:
    foo = par
    bar = slovnik_poctu.get(par)
    zarovnani = 13 - bar
    print(f'{str(foo):>3}', '|', (bar * '*'), '|'.rjust(23 - bar), bar, sep='')
