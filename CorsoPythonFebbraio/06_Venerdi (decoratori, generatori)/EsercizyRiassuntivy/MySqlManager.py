import mysql.connector

# credenziali db
dbCredentials = ("localhost", "root", "password", "sakila")

def GetMysqlConnection(host: str, user: str, password: str, database: str):
    _ = mysql.connector.connect(
        host=host,
        user=user,
        password=password,  # <--- INSERISCI QUI LA TUA PASSWORD DI ROOT
        database=database            # <--- IL NOME DEL TUO DB (es. sakila)
    )
    return _

# restituirà una lista di tuple
# attributes si aspetta una lista di stringhe, es. ["title", "release_year", "rating"] se non passi nulla seleziona tutto (*)
def GetTuplesFromQuery(conn, table: str, attributes = ["*"], maxResults: int=None) -> list:
    
    result = []
    if conn.is_connected():
        print("Connessione al database riuscita!\n")
    
        # 2. Crea il cursore
        cursor = conn.cursor()
        query = f"SELECT {', '.join(attributes)} FROM {table} LIMIT {maxResults};"
            

        # Esegui la query
        cursor.execute(query)

        # Prendi tutti i risultati (ottieni una lista di tuple sql)
        sqlTupleList = cursor.fetchall()

        #  
        for element in range(len(sqlTupleList)):
            #genera una copia delle tupla con i dati che mi interessano
            result.append(sqlTupleList[element])

    return result

def GetColumnNames(conn, table: str) -> list:
    columnNames = []
    if conn.is_connected():
        print("Connessione al database riuscita!\n")
    
        # 2. Crea il cursore
        cursor = conn.cursor()
        query = f"SELECT * FROM {table} LIMIT 1;"
            

        # Esegui la query
        cursor.execute(query)

        # Prendi i nomi delle colonne
        columnNames = [i[0] for i in cursor.description]

    return columnNames