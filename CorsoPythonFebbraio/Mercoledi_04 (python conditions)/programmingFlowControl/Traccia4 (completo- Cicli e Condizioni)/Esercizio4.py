"""
Punto 4: Utilizzo di if, while e for insieme Scrivi un sistema che prende in input
una lista di numeri interi che precedente è stata valorizzata dall'utente.
Il sistema deve:
    1. Utilizzare un ciclo for per trovare il numero massimo nella lista.
    2. Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista.
    3.Utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota,
    altrimenti stampare il numero massimo trovato e il numero di elementi nella lista.
"""


listaNum = []
countListaNum = int(input("Inserisci la lunghezza della lista numeri: "))

# PUNTO 1
# generazione della lista by input utente
for i in range(countListaNum):
    print("Inserisci ", i, "elemento della lista ")
    number = int(input())
    listaNum.append(number)

if(len(listaNum)>0):
    maxNum = listaNum[0]
    for j in range(len(listaNum)):
        if listaNum[j] > maxNum:
            maxNum = listaNum[j]




# PUNTO 2
k = 0
count = 0
while(count < len(listaNum)):
    count = count + 1


# PUNTO 3
if(len(listaNum) == 0):
    print("Lista vuota")
else: 
    print(maxNum)
    print(count)