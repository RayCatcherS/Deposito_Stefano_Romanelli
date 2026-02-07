# blocco dei tipi e del valore di default

def saluta(nome:str, messaggio = ""):
    print(f"Ciao {nome} {messaggio}")


# generatori e decoratori

# FUNZIONI GENERATORI (generator functions)
# Un generatore produce valori "uno alla volta" invece di crearli tutti subito.
# È utile per sequenze grandi perché usa meno memoria.

####### ci fanno fare un passaggio alla volta 

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a          # "restituisce" a e mette in pausa la funzione
        a, b = b, a + b  # aggiorna i valori e continua al prossimo giro

# Uso: il generatore si può iterare con un for
for x in fibonacci(20):
    print(x)

print(
    list(fibonacci(20))
)  # Stampa tutti i valori restituiti dal generatore

# yeld restituisce un valore e mette in pausa la funzione,
# mantenendo il suo stato. Quando si chiama di nuovo, 
# riprende da dove era stata interrotta.

# in questo caso a e b sono gli stati della funzione, e ogni volta che yield restituisce a, la funzione si "ricorda" di dove era arrivata e continua da lì al prossimo giro.

# quando si arriva a yeld si ritorna al codice principale
# quando si ritorna alla funzione si riprende da dove era stata interrotta,
# con tutti i valori delle variabili intatti.
# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13

# riflettere su cosa i può creare annidando i generatori
# fibonacci(fibonacci(fibonacci(20)))


def catena_generatori():
    yield from range(1,4)
    yield from range(10,13)


print(list(catena_generatori()))  # Output: [1, 2, 5, 6]