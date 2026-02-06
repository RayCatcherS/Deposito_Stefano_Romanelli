
"""
Esercizio 1:  Condizioni e cicli
Chieda all’utente di inserire un numero intero positivo. 
 
 Usi un ciclo for per stampare tutti i numeri da 1 fino al numero inserito. 
 
 Per ogni numero: 
 
 stampi "pari" se il numero è pari 
 
 stampi "dispari" se il numero è dispari 
 
 
 
 Se l’utente inserisce un numero minore o uguale a zero, il programma deve stampare un messaggio di errore.
 
"""

n = int(input("inserisci un numero intero positivo\n"))

if(n <= 0):
    print("Errore")
else:
    for i in range(1, n + 1): # ciclo su tutti i numeri da 1 a n compreso
        if(i%2 == 0):
            print(i, "è pari")
        else:
            print(i, "è dispari")