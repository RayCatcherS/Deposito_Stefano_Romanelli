"""
3.Avanzato/ Fattori comuni Descrizione:
Chiedi all'utente di inserire due numeri. Il programma dovrebbe determinare e
stampare i fattori comuni di entrambi i numeri. Se non ci sono fattori comuni
oltre 1, dovrebbe stampare "I numeri sono coprimi". La stessa cosa ma anche per
due stringhe (.equal ) e chiedere se deve ripetere ma sono " complementari" solo
se hanno tutte le lettere in comune (es:abs/ sab)
"""

first = int(input("inserisci il primo numero\n"))
second = int(input("inserisci il secondo numero\n"))

min = first

common = []
if(first < second):
    min = first
else:
    min = second

for i in range(1, min + 1):
    
    if(first%i == 0 and second%i == 0):
        common.append(i)


print(common)
if(len(common) == 1 and common[0] == 1): # non esistono fattori comuni
    print("I numeri sono cooprimi")
else:
    print("I fattori comuni sono:")
    for i in range(0, len(common)):
        print(common[i])