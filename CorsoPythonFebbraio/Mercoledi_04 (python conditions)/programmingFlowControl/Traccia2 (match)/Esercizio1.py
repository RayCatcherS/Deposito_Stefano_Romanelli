"""
ESERCIZIO 1) Descrizione: Scrivi un programma che chieda all'utente la sua età. Se l'età è
inferiore a 18 anni, il programma dovrebbe stampare "Mi dispiace, non puoi
vedere questo film".
Altrimenti, dovrebbe stampare "Puoi vedere questo film".
"""

# Esercizio 1
eta = int(input("Inserisci la tua età: "))
abbonamento = input("Hai un abbonamento? (sì/no): ")
isAbbonato = (abbonamento.lower() == "sì")

minorenne = (eta >= 18)
match minorenne:
    case False:
        print("Mi dispiace, non puoi vedere questo film")
    case True:

        match isAbbonato:
            case False:
                print("Mi dispiace, non puoi vedere questo film")
            case True:
                print("Puoi vedere questo film")
    case _:
        print("Errore: età non valida")