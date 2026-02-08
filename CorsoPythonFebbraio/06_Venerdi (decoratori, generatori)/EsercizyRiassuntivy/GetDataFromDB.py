import MySqlManager

def getMovies():
    # Usa l'unpacking (*) per passare le credenziali
    connection = MySqlManager.GetMysqlConnection(*MySqlManager.dbCredentials)
    
    if connection is None:
        print("Impossibile connettersi al DB.")
        return []

    resultsToGet = 10
    table = "film" 

    exit = False
    movieNameAttriutes = MySqlManager.GetColumnNames(connection, table)
    selectedAttributes = []

    print("-" * 50)
    print("Ecco i nomi delle colonne della tabella film:")
    for idx, attributeName in enumerate(movieNameAttriutes):
        print(f"{idx} - {attributeName}")
    
    print("\nSeleziona gli attributi (es. 0, 1...), premi 'q' per finire:")
    
    while not exit:
        if len(selectedAttributes) > 0:
            print(f"Attuali: {selectedAttributes}")
        
        userInput = input("Scelta: ")

        if userInput.lower() == "q":
            if len(selectedAttributes) == 0:
                selectedAttributes = ["*"]
            exit = True
        else:
            try:
                index = int(userInput)
                if 0 <= index < len(movieNameAttriutes):
                    attributeName = movieNameAttriutes[index] 
                    
                    if attributeName in selectedAttributes:
                        print("Già presente.")
                    else:
                        selectedAttributes.append(attributeName) 
                else:
                    print("Indice non valido.")
            except ValueError:
                print("Input non valido.")
    
    # Ora passiamo la lista pulita di stringhe
    filmList = MySqlManager.GetTuplesFromQuery(
        connection,
        table,
        attributes=selectedAttributes,
        maxResults=resultsToGet
    )
    
    connection.close()
    return filmList
