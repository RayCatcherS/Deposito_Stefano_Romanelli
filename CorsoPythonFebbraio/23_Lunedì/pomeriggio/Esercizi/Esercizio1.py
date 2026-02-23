import numpy as np

# creazione array
ar = np.arange(10, 50, dtype='int32')
print(ar)

# check del tipo
print("Tipo: ")
print(ar.dtype)

print("modifica del tipo in: ")
# cambio del tipo
ar2 = np.array(ar, dtype='int64')
print(ar2.dtype)

# stampa dello shape
print("Shape: ")
print(ar2.shape)