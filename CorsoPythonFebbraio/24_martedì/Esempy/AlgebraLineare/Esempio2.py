import numpy as np

# 1. Definiamo il sistema di equazioni:
# 3x + 1y = 9
# 1x + 2y = 8

# Matrice dei coefficienti (A)
A = np.array([[3, 1], [1, 2]])

# Vettore dei risultati (B)
B = np.array([9, 8])

# 2. Risoluzione del sistema Ax = B
# Questa funzione è più efficiente e numericamente stabile rispetto 
# a calcolare l'inversa (A_inv * B).
x = np.linalg.solve(A, B)

print("Soluzione del sistema:")
print(f"x = {x[0]}, y = {x[1]}") 
# Output: [2. 3.]

# --- VERIFICA ---
# Controlliamo se A moltiplicato per la soluzione x restituisce effettivamente B
verifica = np.allclose(np.dot(A, x), B)
print(f"\nLa soluzione è corretta? {verifica}")