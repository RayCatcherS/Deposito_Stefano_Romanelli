import random

"""
1. Esercizio Base: Indovina il numero
Descrizione: Scrivi un programma che genera un numero casuale
tra 1 e 100 (inclusi). L'utente deve indovinare quale numero è
stato generato. Dopo ogni tentativo, il programma dovrebbe
dire all'utente se il numero da indovinare è più alto o più
basso rispetto al numero inserito. Il gioco termina quando
l'utente indovina il numero o decide di uscire.
"""

def generateRandom():
    return random.random(1, 100)

userWinOrExit = False
randomNum = generateRandom()


while(userWinOrExit):
    
    userInput = int(input("Inserisci il numero da indovinare tra 1 e 100, inserisci 0 per uscire"))

    if(userInput == randomNum):
        userWinOrExit = True
        print("Complimenti hai indovinato")
    elif(userInput < randomNum):
        print("Il numero da indovinare è più grande")
    elif(userInput > randomNum):
        print("Il numero da indovinare è più piccolo")
    elif(userInput > 100 or userInput < 0):
        print("il numero inserito è fuori range")
    elif(userInput == 0):
        print("uscita")
        userWinOrExit = True
    else:
        print("errore")

