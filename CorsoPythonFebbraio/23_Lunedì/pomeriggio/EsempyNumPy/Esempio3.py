import numpy as np

# --- ARANGE: Sequenza di numeri ---
# Funziona come range() di Python, ma restituisce un array NumPy
# Sintassi: np.arange(inizio, fine, passo)
arr_sequenza = np.arange(10) 
print("Array creato con arange:", arr_sequenza) 
# Output: [0 1 2 3 4 5 6 7 8 9]

# --- RESHAPE: Cambiare la forma ---
# Cambia la struttura (dimensioni) senza toccare i dati contenuti
arr_lineare = np.arange(6) # Crea: [0, 1, 2, 3, 4, 5]

# Trasformiamo l'array 1D in una matrice 2D (2 righe, 3 colonne)
reshaped_arr = arr_lineare.reshape((2, 3))

print("Array dopo il reshape (2x3):")
print(reshaped_arr)
# Output:
# [[0 1 2]
#  [3 4 5]]

# Nota: Il prodotto delle dimensioni (2 * 3) deve essere uguale 
# al numero totale di elementi originale (6).