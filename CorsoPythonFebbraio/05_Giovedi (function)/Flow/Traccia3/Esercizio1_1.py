def is_prime(n):
    dividers = []
    isPrime = False

    for i in range(1, n+1): # cercare i divisori
        if(n%i == 0):
            dividers.append(i)
    if(len(dividers)==1):
        isPrime = True
    elif(len(dividers)>2):
        isPrime = False

    elif(len(dividers)== 2):

        if(dividers[0] == 1 and dividers[1] == n):
            isPrime = True
    return isPrime
"""
Scrivi un programma che esegua le seguenti operazioni:
"""


"""
Chiedi all'utente di inserire un numero intero positivo n. 
Se l'utente inserisce un numero negativo o zero, 
continua a chiedere un numero fino a quando non viene inserito un numero positivo.
"""
import random

randomNumbers = ()
listNum = -1
while(listNum<=0):
    listNum = int(input("inserisci un numero"))

"""
Genera una lista di numeri interi casuali tra 1 e n (incluso). 
La lunghezza della lista deve essere n.
"""
print("-------generazione e stampa lista casuale-------")
randListTemp = []
for i in range(listNum):
    randListTemp.append(random.randrange(1,listNum))
randomNumbers = randListTemp
print(randomNumbers)

"""
Utilizza un ciclo for per calcolare e stampare la somma dei numeri pari nella lista.
"""
print("-------stampa tutti i numeri pari nella lista-------")
sumPari = 0
for i in range(listNum ):
    if(randomNumbers[i]%2 == 0):
        sumPari = sumPari + randomNumbers[i]
print("somma pari: ", sumPari)

"""
Utilizza un ciclo for per stampare tutti i numeri dispari nella lista.
"""
print("-------stampa tutti i numeri dispari nella lista-------")
sumDispari = 0
for i in range(listNum):
    if(randomNumbers[i]%2 != 0):
        sumDispari = sumDispari + randomNumbers[i]
print("somma dispari: ", sumDispari)



"""
Utilizza una funzione per determinare se un numero è primo. 
La funzione deve restituire True se il numero è primo, altrimenti False.
"""
print("-------determinare se il num inserito è primo-------")
# determinare se n è primo
dividers = []
isPrime = False

for i in range(1, listNum+1): # cercare i divisori
    if(listNum%i == 0):
        dividers.append(i)
if(len(dividers)==1): # caso il numero è 1 (se stesso e 1)
    isPrime = True
elif(len(dividers)>2): # divisori > 2 => il numero non è primo
    isPrime = False

elif(len(dividers)== 2): # i divisori sono solo due

    if(dividers[0] == 1 and dividers[1] == listNum): # e sono esattamente 1 e se stesso
        isPrime = True

print("il numero n = ",listNum, "è primo: ", isPrime)


"""
Utilizza un ciclo for per stampare tutti i numeri primi nella lista.
"""
print("-------stampare tutti i numeri primi nella lista-------")
for i in range(listNum):
    # determinare se l'i-esimo elemento è primo
    dividers = []
    isPrime = False

    for i in range(1, randomNumbers[i]+1): # cercare i divisori
        if(randomNumbers[i]%i == 0):
            dividers.append(i)
    if(len(dividers)==1):
        isPrime = True
    elif(len(dividers)>2):
        isPrime = False

    elif(len(dividers)== 2):

        if(dividers[0] == 1 and dividers[1] == randomNumbers[i]):
            isPrime = True

    if(isPrime):
        print(randomNumbers[i])

"""
Infine, utilizza una struttura if per determinare se la somma di tutti i numeri 
nella lista è un numero primo e stampa il risultato
"""
print("-------somma di tutti i numeri della lista è primo-------")
totSum = 0
for i in range(listNum):
    totSum = totSum + randomNumbers[i]

dividers = []
isPrime = False

for i in range(1, totSum+1): # cercare i divisori
    if(totSum%i == 0):
        dividers.append(i)
if(len(dividers)==1):
    isPrime = True
elif(len(dividers)>2):
    isPrime = False

elif(len(dividers)== 2):

    if(dividers[0] == 1 and dividers[1] == totSum):
        isPrime = True

print("somma totale è: ", totSum)
if(isPrime):
    print("un numero primo")
else:
    print("un numero non primo")
