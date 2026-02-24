import numpy as np

# 1 genera un array di numeri casuali tra 10 e 50 con dimensione 50

arr = np.random.randint(10, 50, size=50)
arr_original = np.copy(arr) # copia dell'array



# 2 - slicing primi 10 elementi
print("primi 10:\n", arr[:10])

# 3 - slicing ultimi 5
print("ultimi 5 elementi:\n", arr[-5:])

# 4 - slicing dall'indice 5 al 15
print("dall'indice 5 al 15:\n", arr[5:15])

# 5 - slicing ogni 3 elemento
print("slicing elementi con step 3:\n", arr[::3])

# 6 - modifica tramite slicing elementi dall'indice 5 al 10 con valore 99
arr[5:10] = 99
print("modifica slicing:\n", arr)

# array originale 
print("Array originale non modificato:\n", arr_original)