import numpy as np

# Creazione di un array di test
arr = np.array([10, 20, 30, 40, 50])

# --- FANCY INDEXING CON ARRAY ---
# Creiamo un array che contiene le POSIZIONI (indici) che ci interessano
indices_arr = np.array([1, 3]) 

# Estraiamo l'elemento all'indice 1 (20) e all'indice 3 (40)
print("Selezione tramite array di indici:", arr[indices_arr]) 
# Output: [20 40]

# --- FANCY INDEXING CON LISTA ---
# Possiamo usare anche una normale lista Python come "filtro"
indices_list = [0, 2, 4]

# Estraiamo gli elementi agli indici 0, 2 e 4
print("Selezione tramite lista di indici:", arr[indices_list])
# Output: [10 30 50]