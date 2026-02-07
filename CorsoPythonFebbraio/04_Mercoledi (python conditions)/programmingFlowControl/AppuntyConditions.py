# IF (Python)
# Esegue un blocco di codice SOLO se la condizione è True.
# Nota: in Python l'indentazione (spazi) è obbligatoria dentro l'if.

numero = 10

if numero > 0:
    print("Il numero è positivo")  # viene eseguito perché 10 > 0 è True
else: 
    print("Il numero non è positivo")




# IF / ELIF / ELSE (Python)
# - if: prima condizione
# - elif: condizioni alternative (controllate solo se le precedenti sono False)
# - else: caso finale, quando tutte le condizioni sono False

numero = 10

if numero > 0:
    print("Il numero è positivo")

    # questo è un controllo "in più" dentro l'if (solo se numero > 0)
    if numero == 100:
        print("wow")

elif numero < 0:
    print("Il numero è negativo")

else:
    print("Il numero è zero")


# MATCH (Python 3.10+)
# match confronta un valore con vari "case" (pattern) ed esegue il blocco
# del primo case che corrisponde. È simile a switch-case, ma più flessibile.

comando = input("Inserisci un comando: ")

match comando:
    case "start":
        print("Avvio...")
    case "stop":
        print("Stop!")
    case "restart":
        print("Riavvio...")
    case "help" | "h":                 # più valori nello stesso case
        print("Comandi: start, stop, restart, help")
    case _:                             # default: qualsiasi altro valore
        print("Comando non riconosciuto")


# WHILE (Python)
# Esegue un blocco di codice FINCHÉ la condizione è True.
# La condizione viene controllata prima di ogni iterazione.
# Nota: l'indentazione è obbligatoria dentro il while.
# si usa quando non si sa a priori quante volte iterare.

conteggio = 0

while conteggio < 5:
    print(conteggio)    # stampa il valore corrente
    conteggio += 1      # aumenta di 1 - logica di rottura


# FOR (Python)
# Serve per iterare su una sequenza/iterabile (lista, stringa, tupla, range, ecc.).
# Ad ogni giro, "elemento" assume il valore dell’elemento corrente.
# si usa quando si sa a priori quante volte iterare.

# Sintassi:
# for elemento in sequenza:
#     blocco indentato

# Esempio 1: lista
numeri = [10, 20, 30]
for n in numeri:
    print(n)  # stampa ogni numero della lista

# Esempio 2: stringa (itera carattere per carattere)
parola = "ciao"
for ch in parola:
    print(ch)

# Esempio 3: range() (genera numeri da 0 a 4)
for i in range(5):
    print(i)


# range() (Python) - super riassunto
# range(start, stop, step) genera una sequenza di interi:
# - start: inizio (default 0)
# - stop: fine ESCLUSA (obbligatorio)
# - step: passo (default 1)

# 1) Solo stop: parte da 0, arriva a stop-1
for i in range(5):
    print(i)          # 0 1 2 3 4

# 2) start e stop: parte da start, arriva a stop-1
for i in range(4, 10):
    print(i)          # 4 5 6 7 8 9

# 3) start, stop, step: incrementa di step
for i in range(0, 10, 2):
    print(i)          # 0 2 4 6 8

# 4) step negativo: conta all’indietro
for i in range(5, 0, -1):
    print(i)          # 5 4 3 2 1