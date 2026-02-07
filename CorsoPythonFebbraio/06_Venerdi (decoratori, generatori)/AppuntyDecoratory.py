# DECORATORI (Python)
# Un decoratore è una funzione che "avvolge" un’altra funzione per aggiungere
# comportamento prima/dopo (o modificare) senza cambiare il codice originale.
# Si applica con @nome_decoratore sopra la funzione.

# caso in cui si vuole fare un override solo di una parte di codice
def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione della funzione")
        funzione()  # chiama la funzione originale
        print("Dopo l'esecuzione della funzione")
    return wrapper  # ritorna la nuova funzione "modificata"

@decoratore 
def saluta():
    print("Ciao!")

# si possono anche impilare
#@decoratore 
#@decoratore 
#def saluta():
#    print("Ciao!")


@decoratore # si può decorare più volte
def esci():
    print("Esco!")

saluta()

# la funzione saluta ed esci è stata wrappata da "decoratore"


