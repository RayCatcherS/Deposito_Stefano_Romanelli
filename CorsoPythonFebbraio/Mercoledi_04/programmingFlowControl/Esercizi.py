"""
ESERCIZIO if - else - elif

1: Creare una serie di condizioni una dentro l'altra che a fronte di un
input per ogni if decidano se farti passare o no ( 3 livelli, fate un
paragone con == )

2: Andare a creare un if con vari elif e un else finale che gestisca un
menu per la selezione di un crud basilare (aggiungi rimuovi elimina )

3: Creare un if con else semplice, dentro l'if inserire una strttura di
creazione di dati ( nome, password, id dato dal sistema a crescere ) e
nell'else il controllo automatico la dove è presente l'accout nel sistema
e solo se si passa dall'else concludere lo script
"""

# Esercizio 1
input("---------- Esercizio 1 ------------")
userInput = input("Inserisci nome utente")
if(userInput == "admin"):
    password = input("Inserisci password")
    if(password == "1234"):
        containerId = input("Inserisci id container docker")
        if(containerId == "0"):
            print("Accesso consentito")
        else:
            print("Accesso negato: id container errato")
    else:
        print("Accesso negato: password errata")



# Esercizio 2
input("---------- Esercizio 2 ------------")
# container docker disponibili
containerIdList = ["id1", "id2", "id3"]

print("Container disponibili:", containerIdList)
print("Scegli un'operazione: \n1. Aggiungi\n2. Modifica\n3. Rimuovi" )
operation = int(input("Inserisci operazione: "))

if(operation == 1):
        # inserimento nuovo container
        newContainerId = input("Inserisci id nuovo container: ")
        containerIdList.append(newContainerId)
        print("Container aggiunto. Container attuali:", containerIdList)
elif(operation == 2):
    # inserimento indice da modificare
    containerIndex = int(input("Inserisci indice del container da modificare"))
    if(containerIndex > 0 and containerIndex <= len(containerIdList)):
        newContainerId = input("Inserisci nuovo id container: ")
        containerIdList[containerIndex - 1] = newContainerId
        print("Container modificato. Container attuali:", containerIdList)
elif(operation == 3):
    # inserimento id da rimuovere
    containerIndex = int(input("Inserisci id del container da rimuovere"))
    if(containerIndex > 0 and containerIndex <= len(containerIdList)):
        containerIdList.remove(containerIndex)
        print("Container rimosso. Container attuali:", containerIdList)
else:
    print("Operazione non esistente")


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