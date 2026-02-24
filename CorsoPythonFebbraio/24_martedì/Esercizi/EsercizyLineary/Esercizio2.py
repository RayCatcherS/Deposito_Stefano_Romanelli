import numpy as np

# 1. Creare una matrice 5x5 con numeri da 1 a 25
# Usiamo arange(1, 26) per avere i numeri e reshape(5, 5) per la forma
matrice = np.arange(1, 26).reshape(5, 5)
print("Matrice 5x5:\n", matrice)

# 2. Estrarre la seconda colonna
# ':' significa tutte le righe, '1' indica la seconda colonna (indice parte da 0)
seconda_colonna = matrice[:, 1]
print("\nSeconda colonna:", seconda_colonna)

# 3. Estrarre la terza riga
# '2' indica la terza riga, ':' significa tutte le colonne
terza_riga = matrice[2, :]
print("Terza riga:", terza_riga)

# 4. Somma della diagonale principale
# np.diag() estrae gli elementi [1, 7, 13, 19, 25]
diagonale = np.diag(matrice)
somma_diagonale = np.sum(diagonale)

print(f"\nElementi diagonale: {diagonale}")
print(f"Somma diagonale principale: {somma_diagonale}")