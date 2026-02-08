import MySqlManager

# Questo modulo contiene funzioni per recuperare dati specifici dal database, in questo caso i film.
def get_film(connection=None) -> list:
    
    if connection is None:
        print("Impossibile ottenere i film: connessione al database non fornita.")
        return []

    resultsToGet = 10
    film_attributes = attribute_selection(connection, SQL_TABLE)
    SQL_TABLE = "film"

    
    # avvio query
    filmList = MySqlManager.get_tuples_from_table(
        connection,
        SQL_TABLE,
        attributes = film_attributes,
        maxResults=resultsToGet
    )
    return filmList

# Funzione per selezionare dinamicamente gli attributi da visualizzare
def attribute_selection(connection, table) -> list:

    exit = False
    movieNameAttriutes = MySqlManager.get_column_names(connection, table)
    attributes = []

    print("-" * 50)
    print(f"Ecco i nomi delle colonne della tabella {table}:")
    for i, attributeName in enumerate(movieNameAttriutes):
        print(f"{i} - {attributeName}")
    
        print("\nSeleziona un attributo alla volta, premi 'q' per confermare la selezione:")
    
    while not exit:
        if len(attributes) > 0:
            print(f"Attuali: {attributes}")
        
        userInput = input("Scelta: ")

        if userInput.lower() == "q":
            if len(attributes) == 0:
                attributes = ["*"]
            exit = True
        else:
            try:
                index = int(userInput)
                if 0 <= index < len(movieNameAttriutes):
                    attributeName = movieNameAttriutes[index] 
                    
                    if attributeName in attributes:
                        print("Già presente.")
                    else:
                        attributes.append(attributeName) 
                else:
                    print("Indice non valido.")
            except ValueError:
                print("Input non valido.")
                
    return attributes