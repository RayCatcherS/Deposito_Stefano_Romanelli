
def triplica(n):
    return n*3


lista= [1,2,3,4]

lista = list(map(triplica, lista))

 #print (list)

def pari(n):
    return n%2 == 0

list = list(filter(pari, lista))

print(list)


# gestione errori

numero = input("inserisci numero")

# aumenta la sicurezza del codice, intercettando errori
try:
    print (int(numero) + 5)

    # sollevare una exception
    if(numero < 5):
        raise Exception("solo numeri maggiori di 5")
except ValueError as e:
    print("errore inserimento: ", e)
except ZeroDivisionError as e: # errore specifico
    print("errore stai dividendo per zero", e)
except: # errore generico (come negli else)
    print("errore")
finally: # qualsiasi cosa venga eseguito verrà usato il finally
    print("andato tutto a buon fine")

print("eseguo programma")