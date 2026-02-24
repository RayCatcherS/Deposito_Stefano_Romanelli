import numpy as np

# Creazione dell'array di test
arr = np.array([1, 2, 3, 4, 5])

# --- OPERAZIONI STATISTICHE ---

# 1. Somma: addiziona tutti gli elementi
sum_value = np.sum(arr) 

# 2. Media (Mean): calcola il valore medio aritmetico
mean_value = np.mean(arr)

# 3. Deviazione Standard (Standard Deviation): 
# Indica quanto i numeri sono "distanti" o "dispersi" rispetto alla media.
std_value = np.std(arr)

# Visualizzazione dei risultati
print("Sum:", sum_value)              # Output: 15
print("Mean:", mean_value)            # Output: 3.0
print("Standard Deviation:", std_value) # Output: 1.4142135623730951