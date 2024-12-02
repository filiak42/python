'''
prvni_cislo = 5
druhe_cislo = 5

def vynasob(num_1, num_2):
    return num_1 * num_2

vysledek = vynasob(prvni_cislo, druhe_cislo)
print(vysledek)


# Vytvor promennou a uloz zadanou hodnotu
vstup = "Ahoj všem"

# Vytvor funkci ktera vezme string na vstupu
def zdvojnasob_vsechny_znaky(zadani):
    zdvojene = []

    for znak in zadani:
        zdvojene.append(znak * 2)
    return "".join(zdvojene)

# Uloz vystup funkce do promenne vysledek
vysledek = zdvojnasob_vsechny_znaky(vstup)

# Vytiskni vysledek
print(vysledek)


import sys

def je_os_windows():
    return sys.platform.startswith('win')
print(je_os_windows())

'''

# Vytvoř proměnné a ulož do nich zadaná čísla
prvni_cislo = 12
druhe_cislo = 16

def najdi_gcd(x1: int, x2: int) -> int:
    """
    Vrať celočíselnou hodnotu představující největší společný dělitel pro
    parametry "x1" a "x2".
    """
    while x2 > 1:
        zbytek_po_deleni = x1 % x2

        if not zbytek_po_deleni:
            break

        x1, x2 = x2, zbytek_po_deleni
    return x2

# Najdi největšího společného dělitele a ulož jej do proměnné
vysledek = najdi_gcd(prvni_cislo, druhe_cislo)

# Tisk výsledku
print(vysledek)