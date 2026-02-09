# Funzione in cui l'utente può selezionare da una lista di 
# stringa e restituire una tupla di stringhe selezionate. Se l'utente non seleziona nulla, restituisce "*"
def input_select_from_list(elementList) -> tuple:
    exit = False
    selectedElements = []
    
    print("-" * 50)
    print(f"Ecco le opzioni selezionabili:")
    for i, attributeName in enumerate(elementList):
        print(f"{i} - {attributeName}")
    
    print("\nSeleziona un elemento alla volta, premi 'q' per confermare la selezione:")
    while not exit:
        if len(selectedElements) > 0:
            print(f"Attuali: {selectedElements}")
        
        userInput = input("Scelta: ")

        if userInput.lower() == "q":
            if len(selectedElements) == 0:
                selectedElements = ["*"]
            exit = True
        else:
            try:
                index = int(userInput)
                if 0 <= index < len(elementList):
                    attributeName = elementList[index] 
                    
                    if attributeName in selectedElements:
                        print("Già presente.")
                    else:
                        selectedElements.append(attributeName) 
                else:
                    print("Indice non valido.")
            except ValueError:
                print("Input non valido.")

    result = tuple(selectedElements)
    return result

# Funzione in cui l'utente può selezionare un singolo elemento
# da una lista di stringhe e restituirlo. 
# Se l'utente non seleziona nulla, restituisce None
def input_single_select_from_list(elementList) -> str:
    exit = False
    selectedElement = None
    
    print("-" * 50)
    print(f"Ecco le opzioni selezionabili:")
    for i, attributeName in enumerate(elementList):
        print(f"{i} - {attributeName}")
    
    print("\nSeleziona un elemento inserendo il suo numero corrispondente:")
    while not exit:
        userInput = input("Scelta: ")

        try:
            index = int(userInput)
            if 0 <= index < len(elementList):
                selectedElement = elementList[index] 
                exit = True
            else:
                print("Indice non valido.")
        except ValueError:
            print("Input non valido.")

    return selectedElement