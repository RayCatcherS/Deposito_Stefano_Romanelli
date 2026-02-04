# TUPLE (Python)
# Puoi creare una tupla assegnando un insieme di valori separati da virgole
# a una variabile, di solito racchiusi tra parentesi tonde ().
# Le tuple sono simili alle liste, ma in genere si usano per dati "fissi"
# e (a differenza delle liste) non si modificano con append/insert/remove.

punto = (3, 4)                                # tupla con 2 valori (x, y)
colore_rgb = (255, 128, 0)                    # tupla con 3 valori (R, G, B)
informazioni_persona = ("Alice", 25, "Femmina")  # tupla con tipi diversi

# ACCESSO AGLI ELEMENTI
# Si accede agli elementi con l'indice, proprio come nelle liste.
# Gli indici partono da 0.

punto = (3, 4)
print(punto[0])  # stampa il primo elemento -> 3
print(punto[1])  # stampa il secondo elemento -> 4


# errore
# punto = (3, 4) lista di argomenti fissa, non modificabile
# punto[0] = 5

punto = (3, 4) 
# Genera un errore: TypeError



# creazione tupla packing 
punto = 3, 4
x,y = punto # unpacking
print("x: " , x, "y: ", y)

lista = list(punto)