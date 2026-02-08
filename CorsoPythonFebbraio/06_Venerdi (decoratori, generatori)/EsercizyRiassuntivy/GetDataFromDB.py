import MySqlManager

def getMovies():
    
    connection = MySqlManager.GetMysqlConnection(*MySqlManager.dbCredentials)
    # impostazioni query
    resultsToGet = 10
    table = "film" 
    filmList = MySqlManager.GetTuplesFromQuery(
        connection,
        table,
        attributes=["title", "release_year", "rating"],
        maxResults = resultsToGet)
    
    connection.close() # chiudo la connessione al database
    return filmList

