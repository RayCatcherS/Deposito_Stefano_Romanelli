
def lettura(nome_file: str) -> dict[str, list]:
    
    res: dict = {}

    try:
        with open(nome_file, "r") as file:
            raw = file.read()
        

        rows = raw.split("\n")

        for row in rows:
            
            splitted_row = row.split(",")
            
            key = splitted_row[0].strip()
            if key not in res:
                res[key] = []

            for i in range(2, len(splitted_row)):
                res[key].append(splitted_row[i].strip())

    except FileNotFoundError:
        print("Errore: Il file specificato non è stato trovato nella cartella!")
    except Exception as e:
        print(f"Si è verificato un errore inaspettato: {e}")
    finally:
        return res


def modifica_voto(dizionario: dict, student: str, voto_start: int, voto_end: int):

    if student in dizionario:
        votes = dizionario[student]

        for i in range(len(votes)):
            if votes[i] == voto_start:
                votes[i] = voto_end
                return dizionario
        print(f"voto non trovato nella modifica voto di: {student}")
    else:
        print(f"Studente {student} non trovato per la modifica del voto")

    return dizionario

def elimina_studente(dizionario: dict, student: str):

    if student in dizionario:
        del dizionario[student]
    else:
        print(f"Studente {student} non trovato per l'eliminazione")

    return dizionario


def modifica_alunno(dizionario: dict, student:str):

    res:dict = {}

    for k, v in dizionario:
        if k == student:
            votes = dizionario[k]
            dizionario.pop(k)
            dizionario[student] = votes

            res = dizionario
            return res
        
    print(f"Studente {student} non trovato per la modifica dell'alunno")
    return res