"""
2.Intermedio/ Numeri primi in un intervallo :
Chiedi all'utente di inserire due numeri che definiscono un intervallo (es 10 e
50). Il programma dovrebbe stampare tutti i numeri primi compresi in
quell'intervallo o i numeri non primi o entrambi divisi a tua scelta, salvandoli in
due aggregazioni differenti e chiedere se deve ripetere
"""

repeat = True
while (repeat):
    start = int(input("Inserisci partenza intervallo"))
    end = int(input("Inserisci fine intervallo"))
    choice = int(input("Cosa vuoi stampare? 1 pari, 2 dispari"))

    pari = []
    dispari = []
    if(choice == 1 or choice == 2):
        for i in range(start, end):

            if(choice == 1): # stampa i pari
                if(i%2 == 0):
                    pari.append(i)
                    print(i)   
                else:
                    dispari.append(i)

            elif(choice == 2): # stampa i dispari
                if(i%2 != 0):
                    dispari.append(i)
                    print(i) 
                else:
                    pari.append(i)
    else:
        print("scelta non valida")
    
    choose = int(input("Continuare? 1 si, 0 no"))
    if(choose == 1):
        repeat = True
    elif(choose == 2):
        repeat = False
    else:
        print("Errore nella scelta")