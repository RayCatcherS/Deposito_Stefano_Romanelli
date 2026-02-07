"""
break 
contine 
e pass
pagine 83,31 ,80

operatore splat, spalmare nella lista
"""

# break (dentro un for)
# Interrompe subito il ciclo quando si verifica una condizione.

numeri = [1, 2, 3, 4, 5]

for numero in numeri:
    if numero == 3:
        break          # esce dal ciclo quando numero è 3
    print(numero)      # stampa solo finché non incontra 3




# continue (in un ciclo for/while)
# Salta l'iterazione corrente e passa subito alla prossima.

numeri = [1, 2, 3, 4, 5]

for n in numeri:
    if n == 3:
        continue      # quando n è 3, non esegue il print e va al giro dopo
    print(n)

# Output:
# 1
# 2
# 4
# 5



# pass (in Python)
# Non fa nulla: è un "segnaposto" per avere un blocco valido (evita errori di sintassi).
# Utile quando vuoi lasciare una parte vuota per ora.

x = 10

if x > 0:
    pass              # qui potresti aggiungere codice più avanti

def funzione_da_fare():
    pass              # funzione vuota (da completare)

# Non produce output: serve solo a "riempire" il blocco.




# Operatore * (splat / unpacking) in Python
# Serve a "spacchettare" (espandere) un iterabile in elementi separati.
# Si usa spesso per:
# - creare liste/tuple a partire da iterabili
# - concatenare liste
# - passare argomenti a funzioni

# Esempio: espandere range dentro una lista
numeri = [*range(1, 11)]
print(numeri)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Altro esempio: unire liste
a = [1, 2]
b = [3, 4]
uniti = [*a, *b]
print(uniti)   # [1, 2, 3, 4]

# Altro esempio: passare valori come argomenti separati a una funzione
valori = (10, 20, 30)
print(*valori)  # stampa: 10 20 30 (come se fosse print(10, 20, 30))
