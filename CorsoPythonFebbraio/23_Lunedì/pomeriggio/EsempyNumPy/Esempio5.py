import numpy as np

# Creazione di un array lineare da 0 a 9
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# --- SLICING DI BASE ---
# Prende gli elementi dall'indice 2 all'indice 7 (escluso)
print("Slicing (2:7):", arr[2:7]) # Output: [2 3 4 5 6]

# --- SLICING CON PASSO (STEP) ---
# Prende un elemento ogni 2, partendo dall'indice 1 fino all'8 (escluso)
print("Slicing con passo 2 (1:8:2):", arr[1:8:2]) # Output: [1 3 5 7]

# --- OMETTERE START E STOP ---
# Se ometti lo 'start', parte dall'inizio (indice 0)
print("Dall'inizio fino a 5:", arr[:5]) # Output: [0 1 2 3 4]

# Se ometti lo 'stop', arriva fino alla fine dell'array
print("Dal 5 fino alla fine:", arr[5:]) # Output: [5 6 7 8 9]

# --- INDICI NEGATIVI ---
# -1 è l'ultimo elemento, -2 il penultimo, e così via.
# Prende gli ultimi 5 elementi
print("Ultimi 5 elementi (arr[-5:]):", arr[-5:]) # Output: [5 6 7 8 9]

# Prende tutto TRANNE gli ultimi 5 elementi
print("Tutto tranne gli ultimi 5 (arr[:-5]):", arr[:-5]) # Output: [0 1 2 3 4]