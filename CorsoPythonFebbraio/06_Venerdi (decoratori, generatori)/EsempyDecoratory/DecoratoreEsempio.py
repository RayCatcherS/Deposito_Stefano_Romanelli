# DECORATORE per misurare il tempo di esecuzione
# Idea: prima chiama la funzione, salva l'orario di inizio e fine,
# poi stampa la differenza (durata).

import time

def calcola_tempo(funzione):
    def wrapper(*args, **kwargs):
        start_time = time.time()                 # tempo iniziale (secondi)
        risultato = funzione(*args, **kwargs)    # esegue la funzione originale
        end_time = time.time()                   # tempo finale
        print(f"Tempo di esecuzione: {end_time - start_time} secondi")
        return risultato                         # ritorna il risultato della funzione
    return wrapper

@calcola_tempo
def calcolo_lento():
    time.sleep(2)              # simula un'operazione lenta (2 secondi)
    print("Calcolo completato")

# Chiamata alla funzione decorata
calcolo_lento()


# il decoratore non rallenta la funzione, ma misura il tempo 
# che impiega ad eseguire
# Tempo di esecuzione: 2.002345561981201 seconds

# il decoratore sostituisce il calcolo iniziale non rallentando la funzione, ma aggiungendo un "wrapper" che misura il tempo di esecuzione.
# lo 0.002 è il tempo del wrapper, mentre i 2 secondi sono il tempo della funzione originale (sleep).

# decoratore serve a testare ad alto livello in python