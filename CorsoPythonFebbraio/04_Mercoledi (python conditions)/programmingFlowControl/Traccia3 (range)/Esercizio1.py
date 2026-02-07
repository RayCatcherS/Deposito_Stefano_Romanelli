"""
Esercizio 1) Chiedi all'utente di inserire un numero. Il programma
dovrebbe quindi fare un conto alla rovescia a partire da
quel numero fino a zero, stampando ogni numero e chiederti
se vuoi ripetere o no.
"""
continua = True;

while(continua):
    countdown = int(input("Inserisci un numero: "))
    for i in range(countdown):
        print(i)
    risposta = int(input("Vuoi continuare? premi 1 - si, 2 - no: "))
    
    if(risposta == 1):
        continua = True
    else:
        continua = False

