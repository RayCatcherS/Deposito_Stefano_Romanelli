"""
ESERCIZIO 1: Creare una serie di condizioni una dentro l'altra che a fronte di un
input per ogni if decidano se farti passare o no ( 3 livelli, fate un
paragone con == )
"""

# Esercizio 1
input("---------- Esercizio 1 ------------")
userInput = input("Inserisci nome utente")
if(userInput == "admin"):
    password = input("Inserisci password")
    if(password == "1234"):
        containerId = input("Inserisci id container docker")
        if(containerId == "0"):
            print("Accesso consentito")
        else:
            print("Accesso negato: id container errato")
    else:
        print("Accesso negato: password errata")