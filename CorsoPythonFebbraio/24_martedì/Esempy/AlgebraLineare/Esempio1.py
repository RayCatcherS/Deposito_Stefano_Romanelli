import numpy as np

# Creazione di una matrice quadrata 2x2
# Nota: solo le matrici quadrate (n x n) possono avere un'inversa
A = np.array([[1, 2], [3, 4]])

# Calcolo dell'inversa della matrice
# Si usa il modulo linalg (Linear Algebra) di NumPy
A_inv = np.linalg.inv(A)

print("Inversa di A:\n", A_inv)

# --- VERIFICA MATEMATICA ---
# Una matrice moltiplicata per la sua inversa deve dare la Matrice Identità (I)
# La matrice identità ha 1 sulla diagonale principale e 0 altrove.
identita = np.dot(A, A_inv)
print("\nVerifica (A * A_inv):\n", np.round(identita))