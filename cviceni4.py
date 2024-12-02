'''
veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
samohlasky = 'aeiouáéíóú'
souhlasky = 'bcčdďfghjklmnňprřsštťvzžcdž'
vysledek = {
    'souhlasky': 0,
    'samohlasky': 0
}

for znak in veta.lower():
    if znak in samohlasky:
        vysledek['samohlasky'] = vysledek.get('samohlasky') + 1
        samohlasek = vysledek['samohlasky']
    elif znak in souhlasky:
        vysledek['souhlasky'] = vysledek.get('souhlasky') + 1
        souhlasek = vysledek['souhlasky']
else:
    print(f"Počet souhlásek: '{souhlasek}' | Počet samohlásek: '{samohlasek}'")

cisla = [1, 2, 3, 4, 5, 6, 7, 8]
suda = 0
licha = 0

for cislo in cisla:
    if cislo % 2 == 0:
        suda += cislo
    else:
        licha += cislo
else:
    vysledek = licha - suda
    print('Rozdil:', vysledek.__abs__())


# Zadaná proměnná
vysledek = []

# Zadané hodnoty: počáteční hodn., konečná hodn., dělitel
start = 3
stop = 9
delitel = 3

if isinstance(start, int) \
        and isinstance(stop, int) \
        and isinstance(delitel, int):
    print("Zadaný rozsah: <", start, ", ", stop, ">", sep="")

    # Iteruj skrze rozsah zadaných čísel
    for number in range(start, stop + 1):
        # .. pokud je vybrané číslo dělitelné hodnotou v prom. "delitel"
        if number % int(delitel) == 0:
            # .. přidej jej do seznamu "vysledek"
            vysledek.append(number)
    # doplň výpis hodnot v proměnné 'vysledek'
    print('Čísla dělitelná', delitel, ':', vysledek)

else:
    print("Zadané vstupy musí být čísla.")
'''

seznam_slov = ["jablko", "pomeranč", "banán", "kiwi", "hruška"]

delky_slov = {
    slovo: len(slovo)
    for slovo in seznam_slov 
}
print(delky_slov)