import numpy as np

# Creazione di un array di base
arr = np.array([1, 2, 3, 4, 5])

# --- INDEXING (Accesso Diretto) ---
# Accede a un singolo elemento tramite la sua posizione (parte da 0)
print("Primo elemento (indice 0):", arr[0]) # Output: 1

# --- SLICING (Affettamento) ---
# Estrae una porzione dell'array. 
# Sintassi: [inizio : fine_esclusa]
print("Slicing dall'indice 1 al 3 (escluso):", arr[1:3]) # Output: [2 3]

# --- BOOLEAN INDEXING (Filtro Intelligente) ---
# Questa è la funzione avanzata: passiamo una condizione all'interno delle quadre.
# NumPy controlla la condizione per ogni elemento e restituisce solo i "True".
print("Elementi maggiori di 2:", arr[arr > 2]) # Output: [3 4 5]

# Cosa succede "sotto il cofano" con arr > 2?
# Crea una maschera di booleani: [False, False, True, True, True]


## IN CONTESTO MULTIDIMENSIONALE

# Creazione di una matrice 3x4 (3 righe, 4 colonne)
arr_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print("matrice originale:\n", arr_2d)

# --- SLICING SULLE RIGHE ---
# Seleziona dalla riga 1 alla 3 (esclusa), ovvero righe 1 e 2
print("Righe 1 e 2:\n", arr_2d[1:3]) 
# Output: [[ 5  6  7  8] [ 9 10 11 12]]

# --- SLICING SULLE COLONNE ---
# Il simbolo ':' prima della virgola significa "prendi TUTTE le righe"
# '1:3' dopo la virgola seleziona le colonne 1 e 2
print("\nTutte le righe, colonne 1 e 2:\n", arr_2d[:, 1:3])
# Output: [[ 2  3] [ 6  7] [10 11]]

# --- SLICING MISTO ---
# Prende dalla riga 1 alla 3 in poi E dalla colonna 1 alla 3 (esclusa)
print("\nSlicing misto (ritaglio centrale basso):\n", arr_2d[1:3, 1:3])
# Output: [[ 6  7] [10 11]]