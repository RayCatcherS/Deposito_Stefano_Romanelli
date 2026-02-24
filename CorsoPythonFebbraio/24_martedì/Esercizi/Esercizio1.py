import numpy as np


# 1 - 
vect = np.arange(50)
rand_vect = np.random.randint(49, 101, size=[50])
conc_vect = np.copy(np.concatenate((vect, rand_vect))) 


print("vettore originale; concatenazione array con valori incrementali con array di valori casuali\n", conc_vect)
print("il cui dtype: ", conc_vect.dtype)
print("e shape:", conc_vect.shape)


# 2 - cambio dtype
float_array = np.copy(np.array(conc_vect, dtype="float64"))

print("cambio type array in: ", float_array.dtype, "\n", float_array)
print("e shape:", float_array.shape)



# 3 - slicing

# primi 10
print("primi 10:\n", float_array[:10])
# ultimi 7
print("ultimi 5 elementi:\n", float_array[-7:])
# dal 5 al 20
print("ultimi 5 elementi:\n", float_array[5:20])
# slicing ogni 3 elemento
print("slicing elementi con step 3:\n", float_array[::4])

# 4 modifica
array5 = np.copy(float_array)
array5[10:15] = 999
print("modifica 999:\n", array5)

# 5 fancy indexing
indices_list = [0, 3, 7, 12, 25, 33, 48]
print("fancy indexing 1:\n", array5[indices_list])

# maschera booleana
mask = np.zeros(array5.shape, dtype=bool)
mask[array5 % 2 == 0] = True

masked_vec = np.copy(array5[mask])
print("array con mask applicata:\n", masked_vec)


avg = np.mean(masked_vec)
print("media masked vect:\n", avg)
greater_than_vec = np.copy(masked_vec[masked_vec > avg])
print("fancy indexing dove i valori > della media del vettore:\n", greater_than_vec)


# 6