import MySqlManager
import Tool.InputOperations

# Questo modulo contiene funzioni per recuperare dati specifici dal database
def get_tuple_from_table(connection=None, table=None) -> tuple:
    
    if connection is None:
        print("Impossibile ottenere i film: connessione al database non fornita.")
        return ()

    if table is None:
        print("Impossibile ottenere i film: nome della tabella non fornito.")
        return ()

    resultsToGet = 10

    # ottieni tutti i nomi delle tabella 
    tableNameAttriutes = MySqlManager.get_column_names(connection, table)
    
    # chiedi all'utente quali attributi vuole selezionare
    attributes = Tool.InputOperations.input_select_from_list(tableNameAttriutes)
    
    # avvio query
    filmList = MySqlManager.get_tuples_from_table(
        connection,
        table,
        attributes = attributes,
        maxResults=resultsToGet
    )

    result = tuple(filmList)
    return result



