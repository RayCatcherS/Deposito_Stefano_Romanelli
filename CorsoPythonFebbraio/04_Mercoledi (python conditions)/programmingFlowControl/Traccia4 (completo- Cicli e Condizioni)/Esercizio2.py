"""
Punto 2: Utilizzo di while e range
Scrivi un sistema che prende in input un numero intero positivo n e stampa tutti i
numeri da n a 0 (compreso), decrementando di 1.Deve potersi ripete all'infinito
"""


while(True):
    numToCountdown = int(input("Inserisci numero da countdownare"))

    for i in range(numToCountdown):
        print(i)