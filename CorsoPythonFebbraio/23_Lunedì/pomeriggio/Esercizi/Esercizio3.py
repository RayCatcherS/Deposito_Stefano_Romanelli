import numpy as np

# 1 - matrice 2d 6x6 con valori casuali da 1 a 100
mat1 = np.random.randint(1,100, size=[6,6])



# 2 - estrazione sotto matrice
mat2 = np.copy(mat1[1:5, 1:5])


# 3 - inverti le righe della sotto matrice
mat3 = np.copy(np.flip(mat2, axis= 0)) # inverte le righe


# 4 - estrarre la diagonale principale della sotto matrice invertita
diag = np.diag(mat3)


# 5 - sostituire tutti gli elementi della matrice invertita multipli di 3
# con valore -1
mat4 = np.copy(mat3)
mat4[mat4 % 3 == 0] = -1


# 6 - stampa delle matrici

print("matrice generata\n", mat1)
print("sotto matrice 4x4:\n", mat2)
print("matrice 4x4 righe invertite:\n", mat3)
print("diagonale matrice con righe invertite:\n", diag)
print("sostituzione -1 ai valori multipli di 3 nella matrice invertita:\n", mat4)