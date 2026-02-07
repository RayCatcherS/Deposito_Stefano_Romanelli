"""
ESERCIZIO 2: Andare a creare un if con vari elif e un else finale che gestisca un
menu per la selezione di un crud basilare (aggiungi rimuovi elimina )
"""

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