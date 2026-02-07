# LISTE (Python)
# Puoi creare una lista assegnando un insieme di valori separati da virgole
# a una variabile, racchiusi tra parentesi quadre [].

numeri = [1, 2, 3, 4, 5]                 # lista di interi
nomi = ["Alice", "Bob", "Charlie"]       # lista di stringhe
misto = [1, "due", True, 4.5]            # lista con tipi diversi

# ACCESSO AGLI ELEMENTI
# Si può accedere agli elementi di una lista usando l'indice.
# Gli indici partono da 0 (quindi il primo elemento ha indice 0).

numeri = [1, 2, 3, 4, 5]
print(numeri[0])  # stampa il primo elemento -> 1
print(numeri[2])  # stampa il terzo elemento -> 3

# Output atteso:
# 1
# 3

listaMista = [numeri, nomi, misto]




# LISTE - Metodi utili
# Python offre vari metodi/funzioni per lavorare con le liste:
# - len(lista): restituisce la lunghezza della lista
# - append(x): aggiunge x alla fine
# - insert(i, x): inserisce x in posizione i (spostando gli altri a destra)
# - remove(x): rimuove la prima occorrenza di x
# - sort(): ordina la lista (di default in ordine crescente)

numeri = [3, 1, 4, 2, 5]

print(len(numeri))     # lunghezza della lista: ci sono 5 elementi

numeri.append(6)       # aggiunge 6 alla fine
print(numeri)          # [3, 1, 4, 2, 5, 6]

numeri.insert(2, 10)   # inserisce 10 in posizione 2 (terzo posto)
print(numeri)          # [3, 1, 10, 4, 2, 5, 6]

numeri.remove(4)       # rimuove il valore 4 (prima occorrenza)
print(numeri)          # [3, 1, 10, 2, 5, 6]

numeri.sort()          # ordina in modo crescente (modifica la lista "in-place")
print(numeri)          # [1, 2, 3, 5, 6, 10]