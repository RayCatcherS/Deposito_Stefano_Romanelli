import numpy as np

# Creazione di un array 1D
arr = np.array([1, 2, 3, 4])
scalar = 10

# --- IL CONCETTO DI BROADCASTING ---
# NumPy "espande" virtualmente lo scalare 10 per farlo diventare [10, 10, 10, 10]
# In questo modo può eseguire la somma elemento per elemento.
result = arr + scalar

print("Risultato del broadcasting:", result) # Output: [11 12 13 14]