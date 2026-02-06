# Funzioni (usate per l'astrazione)
# blocchi codice autonomo per eseguire porzioni di codice specifiche

    # - modularità
    # - riutilizzo
    # - architettura
    # - manutenibilità (modifica solo nella porzione di codice)

# codice riutilizzabile e leggibile

# funzioni con:
    # return
    # senza

# return implicito è run
def saluta(nome):
    print("ciao,", nome)

# funzioni con lettera minuscola
# argomenti, parametri della funzione (possono essere n)

saluta("stefano")


# VALORE DI RITORNO (return)
# Una funzione può restituire un valore con return.
# Se non usi return (o non specifichi un valore), la funzione restituisce None.

def quadrato(numero):
    return numero * numero   # restituisce il quadrato del numero

risultato = quadrato(4)      # salva il valore restituito
print(risultato)             # 16

# con blocco tipizzazione
def quadrato(numero:int):
    return numero * numero   # restituisce il quadrato del numero

risultato = quadrato(4)      # salva il valore restituito
print(risultato)             # 16



# ordine nei parametri importante!
# possiamo passarli con nome della keyword!


def saluta(nome, messaggio="Ciao"): # qui valori di dafault
    print(f"{messaggio} {nome}!")

saluta("stefano")