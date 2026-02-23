import numpy as np

# --- DTYPE: Specifica il tipo di dati ---
# Il dtype definisce la natura degli elementi (int, float, bool, ecc.)
# Possiamo forzare un tipo specifico in fase di creazione
arr_int = np.array([1, 2, 3], dtype='int32') 
print("Dtype specificato:", arr_int.dtype)  # Output: int32

# --- SHAPE: Le dimensioni dell'array ---
# La shape è una tupla che indica il numero di elementi per ogni asse
# Esempio con una matrice (2D):
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Output: (2, 3) -> Significa 2 righe e 3 colonne
print("Shape dell'array:", arr_2d.shape) 

# --- ESEMPI PRATICI DI SHAPE ---
# Array 1D: (5,)      -> 5 elementi in una riga
# Array 2D: (2, 3)    -> 2 righe, 3 colonne
# Array 3D: (2, 3, 4) -> 2 matrici, ognuna con 3 righe e 4 colonne