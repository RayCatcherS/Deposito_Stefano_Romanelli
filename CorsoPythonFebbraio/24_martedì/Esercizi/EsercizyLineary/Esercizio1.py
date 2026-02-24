import numpy as np

# 1. Creazione dell'array
# Utilizziamo randint per generare numeri INTERI casuali tra 1 e 100
# Il parametro 'size' definisce il numero di elementi (15)
arr = np.random.randint(1, 101, size=15)

# 2. Calcolo della Somma
# np.sum() somma tutti i valori presenti nel vettore
somma_totale = np.sum(arr)

# 3. Calcolo della Media
# np.mean() divide la somma per il numero di elementi (15)
media_totale = np.mean(arr)

# Stampe dei risultati
print("Array generato:\n", arr)
print("-" * 30)
print(f"Somma totale: {somma_totale}")
print(f"Media totale: {media_totale:.2f}") # .2f arrotonda a due decimali


