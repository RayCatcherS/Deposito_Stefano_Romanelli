import MySqlManager

def getMovies():
    
    connection = MySqlManager.GetMysqlConnection(*MySqlManager.dbCredentials)
    # impostazioni query
    resultsToGet = 10
    table = "film" 

    # ottieni lista di argomenti della tupla che mi interessa (es. titolo, anno, rating)
    
    exit = False
    movieNameAttriutes = MySqlManager.GetColumnNames(connection, table)
    selectedAttributes = []

    print("-" * 50)
    print("Ecco i nomi delle colonne della tabella film:")
    for i in range(len(movieNameAttriutes)): # visualizza indice e nome colonna
        print(f"{i} - {movieNameAttriutes[i]}")
    
    print("Seleziona gli attributi che vuoi vedere (es. 0, 1, 2 per titolo, anno, rating), premi q per continuare:")
    while not exit:
        # visualizza attributi selezionati
        if(len(selectedAttributes) > 0):
            print(f"Attributi selezionati: {[movieNameAttriutes[i] for i in selectedAttributes]}")
        else:
            print("Nessun attributo selezionato.")
        
        userInput = input("Inserisci la tua scelta: ")

        if userInput == "q":
            if len(selectedAttributes) == 0:
                selectedAttributes = ["*"]
            exit = True
        else:
            index = int(userInput)
            if index < 0 or index >= len(movieNameAttriutes):
                print("Indice non valido, riprova.")
            elif index in selectedAttributes:
                print("Attributo già selezionato, riprova.")
            else:
                selectedAttributes.append(index)
    

    filmList = MySqlManager.GetTuplesFromQuery(
        connection,
        table,
        attributes = selectedAttributes, # ["title", "release_year", "rating"]
        maxResults = resultsToGet)
    
    connection.close() # chiudo la connessione al database
    return filmList

