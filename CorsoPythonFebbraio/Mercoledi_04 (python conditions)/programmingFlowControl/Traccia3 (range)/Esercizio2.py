"""
Esercizio 2) Chiedi all'utente di inserire un numero.
Il programma dovrebbe controllare se il numero inserito è
primo / pari o no. Se è primo, lo salva e stampa "Il numero
è primo". Altrimenti, stampa "Il numero non è primo".
si ferma il tutto quando ha 5 numeri primi
"""

numeri_pari = []

while len(numeri_pari) < 5:
    numero = int(input("Inserisci un numero: "))
    
    if(numero%2 == 0):
        print("Il numero è pari")
        numeri_pari.append(numero)
    else:
        print("Il numero è dispari")