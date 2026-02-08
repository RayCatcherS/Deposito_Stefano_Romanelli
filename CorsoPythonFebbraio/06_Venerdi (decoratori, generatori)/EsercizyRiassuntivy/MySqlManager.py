import mysql.connector

# Credenziali db
dbCredentials = ("localhost", "root", "password", "sakila")

# Funzione per ottenere una connessione al database MySQL
def get_my_sql_connection(host, user, password, database):
    try:
        return mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    except mysql.connector.Error as err:
        print(f"Errore di connessione: {err}")
        return None

# Funzione per eseguire una query dinamica e restituire i risultati come lista di tuple
def get_tuples_from_table(conn, table: str, attributes=["*"], maxResults: int=None) -> list:
    result = []
    cursor = None # Inizializziamo a None
    
    # Controllo se la connessione esiste ed è aperta
    if conn and conn.is_connected():
        try:
            cursor = conn.cursor()
            
            # Costruzione Query Dinamica
            cols_string = ', '.join(attributes)
            query = f"SELECT {cols_string} FROM {table}"
            
            if maxResults:
                query += f" LIMIT {maxResults}"
            
            # Eseguiamo
            cursor.execute(query)
            
            # fetchall restituisce già una lista di tuple. 
            # Non serve il ciclo for per copiarle una a una!
            result = cursor.fetchall()
            
        except mysql.connector.Error as err:
            print(f"Errore SQL in GetTuplesFromQuery: {err}")
            
        finally:
            if cursor:
                cursor.close()
    
    return result

# Funzione per ottenere i nomi delle colonne di una tabella
def get_column_names(conn, table: str) -> list:
    columnNames = []
    cursor = None
    
    if conn and conn.is_connected():
        try:
            cursor = conn.cursor()
            # Limit 0 è perfetto, ma dobbiamo gestire il cursore dopo
            query = f"SELECT * FROM {table} LIMIT 0;" 
            cursor.execute(query)
            
            # Prendi i nomi
            if cursor.description:
                columnNames = [col[0] for col in cursor.description]
                
            # --- PUNTO CRUCIALE 2: PULIZIA ---
            # Anche se non ci sono righe, dobbiamo dire a MySQL che abbiamo finito
            cursor.fetchall() 
            
        except mysql.connector.Error as err:
            print(f"Errore recupero colonne: {err}")
            
        finally:
            if cursor:
                cursor.close()

    return columnNames