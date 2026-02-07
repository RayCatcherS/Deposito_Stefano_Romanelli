"""
Descrizione: Scrivi un programma che chieda all'utente di inserire un numero
intero positivo n. Il programma deve poi eseguire le seguenti operazioni:

1. Utilizzare un ciclo while per garantire che l'utente inserisca un numero
positivo. Se l'utente inserisce un numero negativo o zero, il programma deve
continuare a chiedere un numero fino a quando non viene inserito un numero
positivo.
2. Utilizzare un ciclo for con range per calcolare e stampare la somma dei
numeri pari da 1 a n.
3. Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n.
4.Utilizzare una struttura if per determinare se n è un numero primo. Un numero
primo è divisibile solo per 1 e per se stesso. Il programma deve stampare se
n è primo o no.
"""

"""
    EXTRA: andare a creare una lista che salva tutti
    i tentativi e un ultima sezione del programma
    che permetta di visionare o modificare la lista
"""

exit = False
log = []

while(not(exit)):

    menu = int(input("1 per inserire numero, 2 visualizzare il log, 3 per eliminare un elemento dal log, 4 per uscire"))
    
    # inserimento numero
    if(menu == 1):
        isPositive = False
        n = 0

        #fin quando l'input non è positivo
        while(not(isPositive)):
            n = int(input("inserisci n positivo"))
            log.append(n)
            if(n > 0):
                isPositive = True
            else:
                isPositive = False
        
        # calcolare e stampare la somma dei numeri pari da 1 a n
        totSum = 0
        for i in range(n + 1):
            if(i%2 == 0):
                totSum = totSum + i 

        message = "La somma dei pari da 1 a " + str(n) + ": " + str(totSum)
        print(message)
        log.append(message)

        print(totSum)



        
        # calcolare e stampare la somma dei numeri dispari da 1 a n.
        totSum = 0
        for i in range(n+1):
            if(i%2 != 0):
                totSum = totSum + i 

        message = "La somma dei dispari da 1 a n: " + str(n) + ": " + str(totSum)
        print(message)
        log.append(message)

        # determinare se n è primo
        dividers = []

        for i in range(1, n+1): # cercare i divisori
            if(n%i == 0):
                dividers.append(i)
        print(dividers)

        isPrime = False
        if(len(dividers)==1):
            isPrime = True
        elif(len(dividers)>2):
            isPrime = False

        elif(len(dividers)== 2):

            if(dividers[0] == 1 and dividers[1] == n):
                isPrime = True

        message = ""
        if(isPrime):
            message = "Il numero è primo"
            
        else:
            message = "Il numero non è primo"
        print(message)
        log.append([n, message])
    elif(menu == 2):
        print(log)
    elif(menu == 3):

        validIndex = False

        while(not(validIndex)):
            indexToRemove = int(input("inserisci quale indice del logo eliminare"))

            if(indexToRemove < 0 or indexToRemove > len(log)):
                print("indice non valido")
                validIndex = False
            else:
                validIndex = True
                log.pop(indexToRemove)
    elif(menu == 4):
        exit = True
    else:
        print("scelta non valida")

    