import numpy as np

# 1. Crea un array di 12 numeri equidistanti tra 0 e 1
arr_lin = np.linspace(0, 1, 12)
print("Array originale (12 elementi):\n", arr_lin)

# 2. Cambia la forma dell'array a una matrice 3x4
# (3 righe * 4 colonne = 12 elementi, quindi il reshape è possibile)
matrice_reshed = arr_lin.reshape(3, 4)
print("\nMatrice 3x4 (da linspace):\n", matrice_reshed)

# 3. Genera una matrice 3x4 di numeri casuali tra 0 e 1
# Usiamo rand(righe, colonne)
matrice_rand = np.random.rand(3, 4)
print("\nMatrice 3x4 (casuale):\n", matrice_rand)

# 4. Calcola e stampa la somma degli elementi di entrambe le matrici
somma_lin = np.sum(matrice_reshed)
somma_rand = np.sum(matrice_rand)

print("\n--- RISULTATI SOMME ---")
print(f"Somma matrice linspace: {somma_lin:.2f}")
print(f"Somma matrice casuale:  {somma_rand:.2f}")