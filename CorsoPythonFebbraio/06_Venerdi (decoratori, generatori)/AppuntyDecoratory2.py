################# decoratori con argomenti #######################

# DECORATORI con argomenti (*args, **kwargs)
# Il decoratore "avvolge" una funzione senza modificarne il codice.
# Il wrapper è la funzione interna che:
# - esegue codice PRIMA e DOPO la funzione originale
# - chiama la funzione originale
# - può leggere/modificare argomenti e/o risultato
# Usa *args e **kwargs per accettare qualsiasi numero di parametri.

def decoratore_con_argomenti(funzione):
    def wrapper(*args, **kwargs):
        print("Prima")
        risultato = funzione(*args, **kwargs)  # chiama la funzione originale con gli stessi argomenti
        print("Dopo")
        return risultato                        # restituisce il risultato originale (o uno modificato)
    return wrapper

@decoratore_con_argomenti
def somma(a, b):
    print(a + b)    # stampa la somma
    return a + b    # restituisce la somma

print("risultato è", somma(3, 4))

# magari viene chiesto di fare controlli sugli argomenti prima di chiamare la funzione originale,
# questo per non toccare la funzione principale, ma solo il decoratore che la avvolge.
# magari in un team ognuno può scrivere la sua funzione principale, 
# e poi si può decidere di decorarla con un decoratore che fa dei controlli sugli argomenti, 
# o che aggiunge del comportamento prima o dopo la funzione originale, 
# senza dover modificare il codice della funzione originale.


##################### FUNZIONI COME ARGOMENTI E RITORNI#######################

# IN PYTHON LE FUNZIONE POSSONO ESSERE PASSATE COME ARGOMENTI AD ALTRA FUNZIONE,
# E POSSONO ANCHE ESSERE RITORNATE DA ALTRA FUNZIONE,
# QUESTO È IL FONDAMENTO DEI DECORATORI, CHE SONO 
# FUNZIONI CHE PRENDONO IN INGRESSO UN'ALTRA FUNZIONE, 
# LA MODIFICANO O AGGIUNGONO COMPORTAMENTO, E LA RITORNANO.


######################## FUNZIONI ANNIDATE ########################
# LE FUNZIONI POSSONO ESSERE DEFINITE DENTRO AD ALTRA FUNZIONE,
# QUESTO È UTILE PER CREARE DECORATORI, O PER CREARE FUNZIONI CHE HANNO UNO STATO INTERNO CHE VIENE MANTENUTO TRA LE CHIAMATE.


########################## RESTITUZIONE FUNZIONE MODIFICATA ##########################
# i decoratori restituiscono una nuova funzione che sostituisce quella originale,
# ma che ha un comportamento modificato, senza modificare il codice originale della funzione decorata.


################ USO DI *ARGS E **KWARGS NEI DECORATORI ################
# questi vengono utilizzati per garantire che il decoratore possa
# gestire funzioni di qualsiasi tipo, con qualsiasi numero di argomenti posizionali e keyword,

################## SINTASSI DECORATORI #####################
# si applica con @nome_decoratore sopra la funzione da decorare,
# è equivalente a scrivere funzione = decoratore(funzione) dopo la definizione della funzione.



