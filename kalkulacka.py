# TODO: vypsani nabidky
def zobraz_nabidku():
    options = ["+", '-', '*', '/', 'pow', 'avg', 'quit']
    spojeni = ' | '.join(options)
    cara = '-' * len(spojeni)
    print(cara, spojeni, cara, sep='\n')

#zobraz_nabidku()

# TODO: prumer
def vypocti_prumer():
    list_cisel = []
    while (cislo := input('Zadej cislo: ')) != '=':
        if cislo.isnumeric():
            list_cisel.append(int(cislo))

    vysledek = sum(list_cisel) / len(list_cisel)
    print(vysledek)

#vypocti_prumer()

# TODO: umocnovani
def umocnovani():
    x1 = int(input('Zadej mocnence: '))
    x2 = int(input('Zadej mocnitele: '))
    vysledek = x1 ** x2
    print(vysledek)

#umocnovani()

# TODO: zakladni matematicke operace


# TODO: zakladni funkce kalkulacka
def kalkulacka():
    while True:
        zobraz_nabidku()

        vyber = input('Vyber funkci:')
        if vyber == 'quit':
            print('Ukoncuji kalkuacku')
            break
        elif vyber == 'avg':
            vypocti_prumer()
        elif vyber == 'pow':
            umocnovani()

kalkulacka()
# TODO: sinus
# TODO: cosinus