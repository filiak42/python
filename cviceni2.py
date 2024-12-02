#ZAMESTNANCI

zamestnanci = [
    'František', 'Bruno',
    'Anna', 'Jakub',
    'Klára', 'Anežka',
    'Anežka', 'Anežka'
]
posledni_index = len(zamestnanci) - 1
print('Na indexu 2 je: ' + zamestnanci[2])
print('Na', posledni_index, 'indexu je:', zamestnanci[posledni_index])
print('V intervalu od 2 do 5 je:', zamestnanci[2:6])
print('Každý třetí člen je:', zamestnanci[::3])

#VYPOCET BMI

jmeno = 'Martin'
vyska = 2
vaha = 80
bmi = vaha / vyska ** 2
if bmi > 40:
    kategorie = 'těžká obezita'
elif bmi > 30:
    kategorie = 'obezita'
elif bmi > 25:
    kategorie = 'mírná nadváha'
elif bmi > 18.5:
    kategorie = 'zdravá váha'
else:
    kategorie = 'podvýživa'

print(jmeno, ' tvé BMI je ' + str(bmi) + ', což spadá do kategorie ' + kategorie + '.')

#ZAMESTNANCI 2

zamestnanci = [
    'František', 'Anna', 'Jakub', 'Klára',
]
print('Zaměstnanci na začátku:', zamestnanci)
zamestnanci_a = zamestnanci.copy()
zamestnanci_a.append('Bruno')
zamestnanci_a.append('Anežka')
print('Nová jména přidána:', zamestnanci_a)
zamestnanci_b = zamestnanci.copy()
zamestnanci_b.insert(1, 'Bruno')
print('Nová jména vlozena:', zamestnanci_b)

#CISLO DNE

vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]
tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')

cislo_dne = int(input('Zadej cislo dne: '))
if vstupni_cisla.__contains__(cislo_dne):
    print('Správná vstupní hodnota!')
    den_tydne = cislo_dne - 1
    if tyden[den_tydne].startswith(vstupni_pismena[den_tydne]):
        print('"Správné písmeno"')
else:
    print('Špatná vstupní hodnota!')