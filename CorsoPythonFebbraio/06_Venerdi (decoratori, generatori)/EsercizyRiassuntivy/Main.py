import GetDataFromDB

filmList = GetDataFromDB.getMovies()

print(f"Ho trovato {len(filmList)} risultati. Ecco i primi 10:")
print("-" * 50)

print(filmList)
