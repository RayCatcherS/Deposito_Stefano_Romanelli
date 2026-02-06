"""
3.Avanzato/ Fattori comuni Descrizione:
Chiedi all'utente di inserire due numeri. Il programma dovrebbe determinare e
stampare i fattori comuni di entrambi i numeri. Se non ci sono fattori comuni
oltre 1, dovrebbe stampare "I numeri sono coprimi". La stessa cosa ma anche per
due stringhe (.equal ) e chiedere se deve ripetere ma sono "complementari" solo
se hanno tutte le lettere in comune (es:abs/ sab)
"""

menu = int(input("1 fattori comuni, 2 stringhe complementari"))

if(menu == 1):
    first = int(input("inserisci il primo numero\n"))
    second = int(input("inserisci il secondo numero\n"))


    min = first
    common = []
    if(first < second): # stabilire i fattori comuni rispetto al più piccolo dei numeri inseriti
        min = first
    else:
        min = second

    for i in range(1, min + 1):
        if(first%i == 0 and second%i == 0): # verifica se i divide senza resto entrambi i valori numerici
            common.append(i)


    print("i fattori comuni sono: ", common)

    if(len(common) == 1 and common[0] == 1): # non esistono fattori comuni
        print("I numeri sono cooprimi")
    else:
        print("I fattori comuni sono:")
        for i in range(0, len(common)):
            print(common[i])
elif(menu == 2):
    first = input("inserisci la seconda stringa\n")
    second = input("inserisci la prima stringa\n")

    if(len(first) == len(second)):

        set1 = set()
        set2 = set()
        for i in range(len(first)):
            set1.add(first[i])
            set2.add(second[i])

        if(set1 == set2):
            print("stringhe complementari")
        else:
            print("stringhe non complementari")

    else:
        print("stringhe non complementari")