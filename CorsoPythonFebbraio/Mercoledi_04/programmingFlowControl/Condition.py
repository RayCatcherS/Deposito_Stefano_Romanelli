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
