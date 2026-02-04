"""
Punto 1: Utilizzo di if
Scrivi un sistema che prende in input un numero e stampa "Pari" se il numero è pari
e "Dispari" se il numero è dispari.
"""

userInput = int(input("inserisci un intero"))
if(userInput%2 == 0):
    print("pari")
else:
    print("dispari")