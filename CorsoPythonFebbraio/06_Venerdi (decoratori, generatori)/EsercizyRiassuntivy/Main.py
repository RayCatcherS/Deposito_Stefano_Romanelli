import GetDataFromDB
import MySqlManager

def main():
    connection = None
    try:
        # Usa l'unpacking (*) per passare le credenziali splat dalla tupla
        connection = MySqlManager.get_my_sql_connection(*MySqlManager.dbCredentials)

        filmList = GetDataFromDB.get_film()

        print(f"Ho trovato {len(filmList)} risultati. Ecco i primi 10:")
        print("-" * 50)

        print(filmList)
    except Exception as e:
        print(f"Si è verificato un errore imprevisto nel programma: {e}")
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Connessione chiusa. Arrivederci!")

main()
