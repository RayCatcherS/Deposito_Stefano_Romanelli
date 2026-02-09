studente = {
    "nome": "Mario",
    "età": 25,
    "sesso": "maschio",
}

print(studente["nome"])
print(studente["età"])

print(studente)


# nuova chiave
studente["corso"] = "Python"
print(studente)

# modifica chiave
studente["età"] = 26
print(studente)

# metodi per i dizionari

# stampa tutte le chiavi
print(studente.keys())

# stampa tutti i valori
print(studente.values())

# stampa tutte le coppie chiave-valore
print(studente.items())


# get non genera un errore se la chiave non esiste, restituisce None
studente.get("nome") # restituisce il valore associato alla chiave "nome"


# pop rimuove la chiave e restituisce il valore associato
studente.pop("sesso") # rimuove la chiave "sesso" e restituisce il valore associato

# remove rimuove la chiave ma non restituisce il valore associato
del studente["corso"] # rimuove la chiave "corso" senza


# cicli di stampa
for chiave in studente.keys():
    print(chiave)

for valore in studente.values():
    print(valore)

for chiave, valore in studente.items():
    print(f"{chiave}: {valore}")

# appartenenza di una chiave
if "nome" in studente:
    print("La chiave 'nome' è presente nel dizionario.")

if "indirizzo" not in studente:
    print("La chiave 'indirizzo' non è presente nel dizionario.")