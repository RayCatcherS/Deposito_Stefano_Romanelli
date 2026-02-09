import Esercizio2_con_extra

class Biblioteca:
    nome = ""
    libri = []
    def __init__(self, nome):
        self.nome = nome
        self.libri = []
    
    def aggiungi_libro(self, libro):
        self.libri.append(libro)
    
    def mostra_libri(self):
        print(f"Libri nella biblioteca {self.nome}:")
        for libro in self.libri:
            print(f"- {libro.titolo} di {libro.autore}")

def inserisci_libri():
    while True:
        input_libro = input("Vuoi aggiungere un libro? (s/n) ")
        if input_libro.lower() == 's':
            titolo = input("Inserisci il titolo del libro: ")
            autore = input("Inserisci l'autore del libro: ")
            pagine = int(input("Inserisci il numero di pagine del libro: "))
            libro = Esercizio2_con_extra.Libro(titolo, autore, pagine)
            biblioteca.aggiungi_libro(libro)
        else:
            break


biblioteca = Biblioteca("Biblioteca Comunale")
print(f"Benvenuto alla {biblioteca.nome}!")
while True:
    input_menu = input("Seleziona un'opzione: 1) Aggiungi libro, 2) Mostra libri, 3) Esci: ")

    if input_menu == "1":
        inserisci_libri()
    elif input_menu == "2":
        biblioteca.mostra_libri()
    elif input_menu == "3":
        print("Arrivederci!")
        break
    else:
        print("Opzione non valida. Riprova.")
