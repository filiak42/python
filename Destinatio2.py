#ZADANI
mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]

ceny = (150, 200, 120, 120, 100, 180)

slevy = ("Olomouc", "Svitavy", "Ostrava")

domeny = ("gmail.com", "seznam.cz", "email.cz")

dvojita_cara = "=" * 35
cara = "-" * 35

nabidka = """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""

AKT_ROK = 2021

#PROGRAM

pozdraveni = 'VITEJTE U NASI APLIKACE DESTINATIO!'
print(pozdraveni)
print(dvojita_cara, end='')
print(nabidka, end='')
print(dvojita_cara)

#INPUT
vyber = int(input('Vyber cislo destinace: '))

if 0 < vyber < 7:
    nazev_destinace = mesta[vyber - 1]
    print('Destinace: ', nazev_destinace.upper())
    print(cara)
else:
    print('Destinace cislo', str(vyber), 'neexistuje!')
    print(cara)
    quit()

#CENA A SLEVA
if nazev_destinace in slevy:
    nova_cena = ceny[vyber - 1] * 0.75
    print('Ziskavate 25% slevu! Nova cena: ' + str(nova_cena) + ',-')
else:
    nova_cena = ceny[vyber - 1]
    print('Jizdenka bez slevy. Cena: ' + str(nova_cena) + ',-')
print(cara)

#JMENO

cele_jmeno = input('Vase cele jmeno: ')
krestni_jmeno = cele_jmeno.split(' ')[0]
if  krestni_jmeno.isalpha():
    print('Krestni jmeno: ' + krestni_jmeno)

else:
    print('Neplatne jmeno')
    print(cara)
    quit()

print(cara)

#OMEZENI PRISTUPU VEK
from datetime import datetime

rok_narozeni = int(input('Vas rok narozeni: '))
current_year = datetime.now().year
vek =  current_year - rok_narozeni

if vek >= 18:
    print('Pristup povolen...')
else:
    print('''Jste prilis mlady na nakup jizdenek!
Ukoncuji program''')
    print(cara)
    quit()

print(cara)

#E-MAIL

e_mail = input('Zapis vasi e-mailovou adresu: ')

if '@' in e_mail and e_mail.split('@')[1] in domeny:
    print('Overeni e-mailu probehlo v poradku.')
else:
    print('''Tento e-mail je neplatny!
Ukoncuji program''')
    print(dvojita_cara)
    quit()

print(dvojita_cara)

#VYSTUPNA ZPRAVA

print('Dekuji,', krestni_jmeno, 'za objednavku jizdenky.')
print('Cilova destinace: ' + nazev_destinace + ', cena jizdneho: ' + str(nova_cena) + ',-')
print('Na Vas e-mail: ' + e_mail + ' jsme odeslali e-jizdenku.')
print(dvojita_cara)