# INSIEMI (set) - Python
# Un insieme (set) è una collezione NON ordinata di elementi UNICI (niente duplicati).
# Puoi creare un set:
# - con set([...]) a partire da una lista (o altra collezione iterabile)
# - oppure con le parentesi graffe { ... }

set1 = set([1, 2, 3, 4, 5])   # crea un set dai valori della lista
set2 = {4, 5, 6, 7, 8}        # crea un set direttamente

# DUPLICATI
# I set non contengono elementi duplicati: se ripeti un valore, viene tenuto una sola volta.

set3 = {1, 2, 3, 3, 4, 4, 5}
print(set3)  # stampa gli elementi senza duplicati

# Nota importante:
# - I set NON hanno indici: non puoi fare set3[0]
# - Inoltre l'ordine di stampa può variare (perché il set è non ordinato)


# operazioni con i set

# INSIEMI (set) - Operazioni base (super riassunto)

A = {1, 2, 3}
B = {3, 4, 5}

# Unione: tutti gli elementi di A e B (senza duplicati)
print(A | B)          # oppure: A.union(B) -> {1, 2, 3, 4, 5}

# Intersezione: solo gli elementi in comune
print(A & B)          # oppure: A.intersection(B) -> {3}

# Differenza: elementi di A che NON sono in B
print(A - B)          # oppure: A.difference(B) -> {1, 2}

# Differenza simmetrica: elementi presenti in uno dei due, ma NON in entrambi
print(A ^ B)          # oppure: A.symmetric_difference(B) -> {1, 2, 4, 5}


