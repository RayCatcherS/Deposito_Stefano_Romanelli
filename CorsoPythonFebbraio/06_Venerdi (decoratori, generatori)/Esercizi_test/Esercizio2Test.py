"""
18.Esercizio 2:  Funzioni e Liste
Definisca una funzione chiamata conta_vocali. 
 
 La funzione deve: 
 
 ricevere una stringa come parametro 
 
 contare quante vocali contiene (a, e, i, o, u) 
 
 restituire il numero totale di vocali 
 
 
 
 Nel programma principale: 
 
 chiedi all’utente di inserire una parola 
 
 chiama la funzione 
 
 stampa il numero di vocali trovate
 
"""

def conta_vocali(stringa: str):
    counter = 0
    vocali = {"a", "e", "i", "o", "u"}
    for i in range(len(stringa)): # per ogni carattere di stringa
        if(stringa[i] in vocali): # se il carattere è nell'insieme delle vocali
            counter = counter + 1
    return counter


print(
    conta_vocali(
        input("Inserisci una parola:\n")
    )
)