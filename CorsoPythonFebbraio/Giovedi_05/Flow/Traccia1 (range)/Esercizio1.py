"""

ESERCIZIO 1. Base / Numeri pari e dispari o sequenza Descrizione:
Scrivi un programma che chiede all'utente di inserire un numero o una stringa
scegliendo prima quale. Il programma dovrebbe determinare se il numero è pari o
dispari e stampare il risultato e se deve ripetere o stampare e poi ripetere.

"""
repeat = True
result = ""
while(repeat):
    menuChoice = int(input("premi \"1\" se vuoi inserire un numero\noppure\npremi \"2\" se vuoi inserire una stringa\n"))

    if(menuChoice == 1):
        num = int(input("Inserisci un numero\n"))

        if(num%2 == 0):
            result = "numero inserito pari"
        else:
            result = "numero inserito dispari"

    elif(menuChoice == 2):
        str = input("Inserisci una stringa\n")
        strlen = len(str)

        if(strlen%2 == 0):
            result = "numero di caratteri pari"
        else:
            result = "numero di caratteri dispari"
    
    print(result)

    menuChoice = int(input("premi \"1\" per ripetere l'inserimento\noppure\npremi \"2\" stampa il risultato e ripeti inserimento\noppure\n premi\"3\" per uscire"))
    if(menuChoice == 2):
        print(result)
    elif(menuChoice == 3):
        break