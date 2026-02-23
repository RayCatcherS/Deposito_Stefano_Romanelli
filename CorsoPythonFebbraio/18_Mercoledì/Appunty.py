# file
# r - read; w - scrittura e sovrascrittura; a - scrittura o aggiunta - x crea il file
# open("Esempio.csv", "r")

# contesto di apertura file
# tutto ciò che sta in questa indentazione riguarda apertura e chiusura
# gestisce la chiusua in modo safe
with open("Esempio.txt", "r") as file:
    contenuto = file.read()


print(contenuto)

""""
# write sovrascrive il contenuto
with open("Esempio.txt", "w") as file:
    file.write("il mio primo file")
"""

# convertire file in matrice
with open("Esempio.txt", "r") as file:
    contenuto = file.read()

righe = contenuto.split("\n")
print(righe)


matrice1 = []
for riga in righe:
    matrice1.append(riga.split(","))

print(matrice1) #lista di liste riga e colonna del contenuto del file csv


# modificare un elemento nella matrice
for riga in range(1, len(matrice1)):
    if matrice1[riga][0] == "stefano":
        matrice1[riga][2] = "nuovo cognome" # sostituisci il cognome

# farlo in una sola riga
# matrice = [riga.split(",") for riga in righe]

listarighe = []
for riga in matrice1:
    listarighe.append(",".join(riga))

# print (listarighe)
# printerà una lista di stringhe con elementi separati da virgola

# IMPORTANTE
# è importante che all'interno del file non vengano fatti cicli ma si facciano solo direttamente
# operazioni di lettura e scrittura