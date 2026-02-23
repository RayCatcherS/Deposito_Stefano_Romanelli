import numpy as np

# --- 1. CREAZIONE DI ARRAY ---

# Creazione da una lista Python standard
arr = np.array([1, 2, 3, 4, 5])

# Altre funzioni comuni di creazione menzionate negli appunti:
# np.zeros((2, 3))     -> Array di zeri (2 righe, 3 colonne)
# np.ones(5)           -> Array di 5 elementi tutti pari a 1
# np.arange(0, 10, 2)  -> Array da 0 a 10 (escluso) con passo 2
# np.linspace(0, 1, 5) -> 5 numeri equispaziati tra 0 e 1

# --- 2. METODI E ATTRIBUTI DI ANALISI ---

# Proprietà strutturali
print("Forma dell'array:", arr.shape)      # Output: (5,) -> Indica la dimensione (es. righe, colonne)
print("Dimensioni (assi):", arr.ndim)      # Output: 1    -> Numero di dimensioni (1D, 2D, ecc.)
print("Tipo di dati:", arr.dtype)          # Output: int64 -> Il tipo di elementi contenuti
print("Numero di elementi:", arr.size)     # Output: 5    -> Totale elementi nell'array

# Operazioni statistiche e di aggregazione
print("Somma degli elementi:", arr.sum())  # Output: 15   -> Somma tutti i valori
print("Media degli elementi:", arr.mean()) # Output: 3.0  -> Calcola la media aritmetica
print("Valore massimo:", arr.max())        # Output: 5    -> Restituisce il valore più alto
print("Indice del massimo:", arr.argmax()) # Output: 4    -> Restituisce la POSIZIONE del valore massimo




