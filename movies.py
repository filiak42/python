oddelovac = "=" * 62

sluzby = ("dostupne filmy", "detaily filmu", 'reziseri', "doporuc film")

uzivatele = {
    "tomas": {"Shawshank Redemption", "The Godfather", "The Dark Knight"},
    "petr": {"The Godfather", "The Dark Knight"},
    "marek": {"The Dark Knight", "The Prestige"}
}

film_1 = {
    "JMENO": "Shawshank Redemption",
    "HODNOCENI": "93/100",
    "ROK": 1994,
    "REZISER": "Frank Darabont",
    "STOPAZ": 144,
    "HRAJI": ("Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
      "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
      "Jeffrey DeMunn", "Larry Brandenburg"
     )
}

film_2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "92/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": ("Marlon Brando", "Al Pacino", "James Caan",
      "Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
      "John Marley", "Richard Conte"
    )
}

film_3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": ("Christian Bale", "Heath Ledger", "Aaron Eckhart",
      "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
      "Monique Gabriela", "Ron Dean", "Cillian Murphy"
    )
}

film_4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": ("Hugh Jackman", "Christian Bale", "Michael Caine",
      "Piper Perabo", "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin",
      "David Bowie"
    )
}

filmy = {
    film_1["JMENO"]: film_1,
    film_2["JMENO"]: film_2,
    film_3["JMENO"]: film_3,
    film_4["JMENO"]: film_4
}

from pprint import pprint

#PRIHLASENI

jmeno = input('ZADEJ JMENO: ')

if jmeno not in uzivatele.keys():
    print('UZIVATEL NEEXISTUJE!')
    quit()
else:
    print('v poradku'.upper(), oddelovac, sep='\n')
    print('vitejte v nasem filmovem slovniku'.upper().center(62), oddelovac, sep='\n')
    print(('| ' + ' | '.join(sluzby) + ' |').center(62), oddelovac, sep='\n')

#VYBER SLUZBY

vyber = input('VYBER SLUZBU: ')
if vyber in sluzby and vyber == 'dostupne filmy':
    print('NASE FILMY:', ', '.join(filmy.keys()))
elif vyber in sluzby and vyber == 'detaily filmu':
    print('NASE FILMY:', ', '.join(filmy.keys()))
    film = input('VYBER FILM: ')
    pprint(filmy.get(film, 'Film neni dostupny!'))
elif vyber in sluzby and vyber == 'reziseri':
    reziseri = {
        filmy["Shawshank Redemption"]["REZISER"],
        filmy["The Godfather"]["REZISER"],
        filmy["The Dark Knight"]["REZISER"],
        filmy["The Prestige"]["REZISER"]
        }
    print(', '.join(reziseri))
elif vyber in sluzby and vyber == 'doporuc film':
    uzivatele_1 = uzivatele.copy()
    set_uzivatele = uzivatele_1.pop(jmeno)
    uzivatel_zbytku_1 = uzivatele_1.popitem()
    uzivatel_zbytku_2 = uzivatele_1.popitem()
    

else:
    print("vybrana sluzba neni v nabidce, ukoncuji..")