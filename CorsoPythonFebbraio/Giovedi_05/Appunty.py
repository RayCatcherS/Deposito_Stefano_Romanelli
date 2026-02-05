"""
break 
contine 
e pass
pagine 83,31 ,80

operatore splat, spalmare nella lista
"""


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
