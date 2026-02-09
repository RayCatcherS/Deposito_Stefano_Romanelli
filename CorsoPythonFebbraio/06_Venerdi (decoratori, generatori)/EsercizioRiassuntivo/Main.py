import GetDataFromDB
import MySqlManager
import Tool.InputOperations

def main():
    connection = None
    try:
        # Usa l'unpacking (*) per passare le credenziali splat dalla tupla
        connection = MySqlManager.get_my_sql_connection(*MySqlManager.dbCredentials)


        print("tabelle disponibili:")
        # Otteniamo i nomi di tutte le tabelle del database
        tables_name = MySqlManager.get_schema_tables_names(connection)

        # l'utente seleziona una stringa da una lista di stringhe (tabelle) 
        selected_table = Tool.InputOperations.input_single_select_from_list(tables_name)

        dbTuples = GetDataFromDB.get_tuple_from_table(connection, selected_table)

        print(f"Ho trovato {len(dbTuples)} risultati:")
        print("-" * 50)

        print(dbTuples)
    except Exception as e:
        print(f"Si è verificato un errore imprevisto nel programma: {e}")
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Connessione chiusa. Arrivederci!")

main()
