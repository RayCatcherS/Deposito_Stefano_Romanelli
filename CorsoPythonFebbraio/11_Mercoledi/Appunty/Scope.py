# --- SCOPE DELLE VARIABILI IN PYTHON ---

# 1. Variabile Globale: definita fuori da ogni funzione.
# È accessibile da ovunque, ma non modificabile dalle funzioni senza 'global'.
numero = 10

def funzione_esterna():
    # 2. Variabile Locale (Enclosing): definita dentro la funzione esterna.
    # Oscura la variabile globale con lo stesso nome solo all'interno di questo blocco.
    numero = 5
    print("Numero dentro funzione_esterna (locale):", numero)

    def funzione_interna():
        # 3. Parola chiave 'nonlocal':
        # Dice a Python di non creare una nuova variabile locale, 
        # ma di usare quella definita nella funzione immediatamente superiore (esterna).
        nonlocal numero
        numero = 3
        print("Numero dentro funzione_interna (nonlocal):", numero)

    # Chiamata alla funzione annidata
    funzione_interna()
    
    # Qui 'numero' è diventato 3 perché la funzione_interna l'ha modificato tramite nonlocal
    print("Numero dentro funzione_esterna dopo chiamata interna:", numero)

# --- ESECUZIONE ---

print("Numero nel main (globale all'inizio):", numero)

# Eseguiamo la catena di funzioni
funzione_esterna()

# La variabile globale NON è stata toccata dalle funzioni sopra
print("Numero nel main dopo chiamata (globale rimane invariato):", numero)