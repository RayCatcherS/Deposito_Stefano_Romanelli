######################## ESEMPIO PRATICO DI DECORATORE ##########################
# usato per logging delle chiamate a funzione

# DECORATORE "logger"
# Scopo: aggiungere logging (stampe) prima/dopo una funzione,
# mostrando nome funzione, argomenti passati e risultato.

def logger(funzione):
    # wrapper: prende QUALSIASI argomento grazie a *args e **kwargs
    def wrapper(*args, **kwargs):
        # __name__ è il nome della funzione originale (es. "moltiplica")
        print(f"Chiamata a {funzione.__name__} con argomenti: {args} e {kwargs}")
        
        risultato = funzione(*args, **kwargs)  # chiama la funzione originale
        
        print(f"Risultato di {funzione.__name__}: {risultato}")
        return risultato  # restituisce lo stesso risultato della funzione originale
    
    return wrapper  # ritorna la versione "decorata" della funzione

@logger
def moltiplica(a, b):
    return a * b

# Chiamata alla funzione decorata
print(moltiplica(3, 4))


# Chiamata a moltiplica con argomenti: (3, 4) e {}
# Risultato di moltiplica: 12
# 12