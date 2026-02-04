"""
ESERCIZIO 3: Creare un if con else semplice, dentro l'if inserire una strttura di
creazione di dati ( nome, password, id dato dal sistema a crescere ) e
nell'else il controllo automatico la dove è presente l'accout nel sistema
e solo se si passa dall'else concludere lo script
"""

# Esercizio 3

print("---------- Esercizio 3 ------------")
# unico utente registrato
registeredUsers = {("stefano", "password", 1), ("pippo", "password", 2)}
idCounter = len(registeredUsers) + 1

# acquisizione dati utente
username = input("Inserisci nome utente: ")
password = input("Inserisci password: ")
id = int(input("Inserisci id utente: "))

# creazione tupla dati utente (richiesta di accesso)
request = (username, password, id)

print("Utente richiesto:", request)

if registeredUsers.__contains__(request) == False:
    # creazione nuovo account
    print("Creazione nuovo account...")
    registeredUsers.add(request)
    idCounter += 1
    print("Account creato con successo")
else:
    # accesso consentito
    print("Accesso consentito")

print("Utenti registrati:", registeredUsers)