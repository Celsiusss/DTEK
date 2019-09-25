"""
INF100 Oblig oppgaver
Av Daniel Liland
"""

# %%
"""
Oppgave 1
"""

print('Gi tre heltall.')
tall1 = int(input('Tall #1: '))
tall2 = int(input('Tall #2: '))
tall3 = int(input('Tall #3: '))

if tall1 < tall2 < tall3:
    print('Tallene er strengt stigende')
elif tall1 > tall2 > tall3:
    print('Tallene er strengt synkende')
else:
    print('Tallene er verken strengt stigende eller strenmgt synkende')

# %%
"""
Oppgave 2.a
"""
print('Konverter hurtignotasjon av korttype.')
kort = input('Skriv inn en bokstav (D, H, S, C): ')
if kort == 'D':
    print('Ruter')
elif kort == 'H':
    print('Hjerter')
elif kort == 'S':
    print('Spar')
elif kort == 'C':
    print('Kløver')
else:
    print('Ikke gyldig')

# %%
"""
Oppgave 2.b
"""
kortVerdier = {
    'A': 'Ess',
    '2': 'To',
    '3': 'Tre',
    '4': 'Fire',
    '5': 'Fem',
    '6': 'Seks',
    '7': 'Syv',
    '8': 'Åtte',
    '9': 'Ni',
    '10': 'Ti',
    'J': 'Knekt',
    'Q': 'Dame',
    'K': 'Konge'
}

kortVerdi = input('Skriv inn en kortverdi:')

if kortVerdi in kortVerdier:
    print(kortVerdier[kortVerdi])
else:
    print('Ikke gyldig kortverdi')

# %%
"""
Oppgave 3.a
"""
kurser = {
    'EUR': 9.91,
    'USD': 9.05,
    'DKK': 1.33
}

print('Valutakonvertering')
print('Konverterer fra en valuta til NOK')
print('Tillate valutaer: EUR, USD, DKK')
valuta = input('Fra valuta: ')
if valuta in kurser:
    valutaMengde = float(input('Mengde: '))
    konvertert = kurser[valuta] * valutaMengde
    print(valuta + ': %.2f' % valutaMengde)
    print('NOK: %.2f' % konvertert)
else:
    print('Valutaen ' + valuta + ' støttes ikke.')

# %%
"""
Oppgave 3.b
"""
print('Valutakonvertering')
print('Konverterer fra NOK til en valuta')
print('Tillate valutaer: EUR, USD, DKK')
valuta = input('Til valuta: ')
if valuta in kurser:
    valutaMengde = float(input('Mengde: '))
    konvertert = valutaMengde / kurser[valuta]
    print('NOK: %.2f' % valutaMengde)
    print(valuta + ': %.2f' % konvertert)
else:
    print('Valutaen ' + valuta + ' støttes ikke.')

# %%
"""
Oppgave 4
"""
for tall in range(0, 10):
    print(tall)
    print(tall ** 3)
    print('\n')

# %%
"""
Oppgave 5
"""
print('Finn alle tall i et intervall som er delelig på N')
start = int(input('Start: '))
slutt = int(input('Slutt: '))
n = int(input('N: '))

delelige = []

print('Verdier mellom ' + str(start) + ' og ' + str(slutt) + ' som er delelig på ' + str(n))
for tallet in range(start, slutt + 1):
    if tallet % n == 0:
        delelige.append(tallet)

if len(delelige) > 0:
    delelige = map(lambda x: str(x), delelige)
    print(', '.join(delelige))
else:
    print('Ingen delelige tall funnet')

# %%
"""
Oppgave 6.a
"""


def til_fahrenheit(celsius: float):
    return (celsius * 1.8) + 32


print('Celsius    Fahrenheit')
for graderCelsius in range(0, 101, 10):
    fahrenheit = round(til_fahrenheit(graderCelsius))
    linje = str(graderCelsius).rjust(7) + str(fahrenheit).rjust(14)
    print(linje)

#%%
"""
Oppgave 6.b
"""


def tilFahrenheit(celsius: float):
    return (celsius * 1.8) + 32


print('Celsius    Fahrenheit         Status')
for graderCelsius in range(0, 101, 10):
    fahrenheit = round(tilFahrenheit(graderCelsius))

    status = 'Jeg har det bra'
    if graderCelsius > 60:
        status = 'Jeg svetter ihjel'

    linje = str(graderCelsius).rjust(7) + str(fahrenheit).rjust(14) + status.center(25)
    print(linje)

#%%
"""
Oppgave 7
"""


def renteOkning(verdi: float, fra: int, til: int):
    antallAr = til - fra
    sluttVerdi = verdi
    for i in range(antallAr + 1):
        sluttVerdi *= 1.02
    return sluttVerdi


print('%.2f' % renteOkning(100, 1910, 2020))
