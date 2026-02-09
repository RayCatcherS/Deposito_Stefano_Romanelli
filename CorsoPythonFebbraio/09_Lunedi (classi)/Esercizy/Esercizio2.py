
class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        return f"Il libro {self.titolo} è stato scritto da {self.autore} e ha ({self.pagine} pagine)"
    
    def __str__(self):
        return f"Libro: {self.titolo} di {self.autore}, {self.pagine} pagine"

# funzione per inserire libri da input
def inserisci_libri():
    while True:
        titolo = input("Inserisci il titolo del libro: ")
        autore = input("Inserisci l'autore del libro: ")
        pagine = int(input("Inserisci il numero di pagine del libro: "))
        
        libro = Libro(titolo, autore, pagine)
        libri.append(libro)
        
        scelta = input("Vuoi inserire un altro libro? (s/n) ")
        if scelta.lower() != 's':
            break

def visualizza_libri():
    for libro in libri:
        print(libro)

# riempimento dei dati da input
libri = []

while True:
    user_input = input("seleziona operazione: 1 inserisci libri, 2 visualizza libri, 3 esci: ")
    if user_input == "1":
        inserisci_libri()
    elif user_input == "2":
        visualizza_libri()
    elif user_input == "3":
        break
    else:
        print("Scelta non valida.")