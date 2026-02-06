"""
2. Esercizio Avanzato: Sequenza di Fibonacci fino a N
Descrizione: Chiedi all'utente di inserire un numero N. Il
programma dovrebbe stampare la sequenza di Fibonacci fino a N.
Ad esempio, se l'utente inserisce 100, il programma dovrebbe
stampare tutti i numeri della sequenza di Fibonacci minori o
uguali a 100.

"""

def successioneFibonacci(n_max):
    i = 0
    j = 1

    while(j < n):
        k = i + j
        print(k)
        i = j
        j = k


n = int(input("inserisci N"))
successioneFibonacci(n)

