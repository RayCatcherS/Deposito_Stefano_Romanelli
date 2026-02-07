"""
ESERCIZIO 2) Descrizione: Scrivi un programma che chieda all'utente di inserire due
numeri e un'operazione da eseguire tra addizione (+), sottrazione (-),
moltiplicazione (*) e divisione (/). Il programma dovrebbe poi eseguire
l'operazione e stampare il risultato. Tuttavia, se l'utente tenta di dividere
per zero, il programma dovrebbe stampare "Errore: Divisione per zero".
Se l'operazione inserita non è riconosciuta, dovrebbe stampare "Operazione
non valida".

"""


# Esercizio 2 
num1 = float(input("primo numero: "))
num2 = float(input("secondo numero: "))
operazione = input("Inserisci l'operazione +, -, *, /:")


match operazione:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case _:
        print("Operazione non valida")