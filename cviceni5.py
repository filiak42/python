'''
slova = []

while len(slova) < 3:
    slovo = input('ZADEJ SLOVO ZE ČTYŘ:')
    if slovo.isalpha() and len(slovo) != 4:
        print('Slovo není dlouhé čtyři znaky')
    elif slovo.isalpha() and slovo in slova:
        print('Slovo', slovo, 'už je uložené')
    elif slovo.isalpha():
        slova.append(slovo)
    else:
        print('Slovo musí obsahovat pouze znaky abecedy')

print('Už mám uložené tři slova')
print(slova)
'''

while True:
    operation = input('''
Sčítání:    "+",
Odčítání:   "-",
----------------------
Vyber si operaci: '''
                )
    if operation not in {'+', '-'}:
        print('Nezadali jste platný operátor, zkuste to znovu.')
        continue
    else:
        number_1 = int(input('Zadej první číslo: '))
        number_2 = int(input('Zadej druhé číslo: '))
    if operation == '+':
        print(f'{number_1} + {number_2} = {number_1 + 
number_2}')
    elif operation == '-':
        print(f'{number_1} - {number_2} = {number_1 - number_2}')

    # Ověř zda chce uživatel pokračovat nebo chce program ukončit
    again = input('Chcete provést další operaci?(a pro ano, jakákoliv jiná klávesa pro ne): ')

    if again == 'a':
        continue
    else:
        print('Ukončuji...')
        break