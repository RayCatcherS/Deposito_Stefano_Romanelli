class Piatto():
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo

class Ristorante:
    aperto = False
    piatti = []
    descrizione = ""
    def __init__(self, nome, tipo_cucina, descrizione):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.descrizione = descrizione
        self.aperto = False
    
    def descrivi_ristorante(self):
        print(f"Il ristorante {self.nome} offre cucina {self.tipo_cucina}. {self.descrizione}\n Attualmente è {'aperto' if self.aperto else 'chiuso'}.")

    def apri_ristorante(self):
        self.aperto = True
        print(f"Il ristorante {self.nome} è ora aperto.")

    def chiudi_ristorante(self):
        self.aperto = False
        print(f"Il ristorante {self.nome} è ora chiuso.")

    def aggiungi_piatto(self):
        nome = input("Inserisci il nome del piatto: ")
        prezzo = float(input("Inserisci il prezzo del piatto: "))
        piatto = Piatto(nome, prezzo)

        self.piatti.append(piatto)
        print(f"Il piatto {piatto.nome} è stato aggiunto al menu del ristorante {self.nome}.")
    
    def rimuovi_piatto(self):

        # visualizza i piatti presenti nel menu
        print("Piatti presenti nel menu:")

        if(len(self.piatti) == 0):
            print("Non ci sono piatti nel menu.")
            return
        # visualizza con indice
        for i, piatto in enumerate(self.piatti):
            print(f"{i}: {piatto.nome} - {piatto.prezzo}€")
        # chiede all'utente l'indice del piatto da rimuovere
        
        
        indice = int(input("Inserisci l'indice del piatto da rimuovere: "))
        if 0 <= indice < len(self.piatti):
            piatto_rimosso = self.piatti.pop(indice)
            print(f"Il piatto {piatto_rimosso.nome} è stato rimosso dal menu del ristorante {self.nome}.")
        else:
            print("Indice non valido.")

    def stampa_menu(self):
        print(f"Menu del ristorante {self.nome}:")
        if(len(self.piatti) == 0):
            print("Non ci sono piatti nel menu.")
            return
        for piatto in self.piatti:
            print(f"{piatto.nome} - {piatto.prezzo}€")

# punto 3 dell'esercizio
ristoranti = []
def gestisci_ristorante(rist: Ristorante):

    def gestisci_inserimento_piatto():
        while True:
            rist.aggiungi_piatto()
            cont = input("Vuoi aggiungere un altro piatto? (s/n): ")
            if cont.lower() != 's':
                break

    while True:
        menu_choice = input("Scegli un'opzione:\n1. Leggi descrizione ristorante\n2. Apri ristorante\n3. Chiudi ristorante\n4. Aggiungi piatto\n5. Rimuovi piatto\n6. Stampa menu\n7. Chiudi gestione ristorante\n")

        if menu_choice == "1":
            rist.descrivi_ristorante()
        elif menu_choice == "2":
            rist.apri_ristorante()
        elif menu_choice == "3":
            rist.chiudi_ristorante()
        elif menu_choice == "4":
            gestisci_inserimento_piatto()
        elif menu_choice == "5":
            rist.rimuovi_piatto()
        elif menu_choice == "6":
            rist.stampa_menu()
        elif menu_choice == "7":
            break

def gestisci_ristoranti():
    
    while True:
        scelta = input("Visualizza ristoranti esistenti (1), Aggiungi nuovo ristorante (2), Gestisci ristorante (3), Esci (4): ")
        if scelta == "1":
            if len(ristoranti) == 0:
                print("Non ci sono ristoranti disponibili.")
            else:
                # viusalizza con indice
                for i, r in enumerate(ristoranti):
                    print(f"{i}: {r.nome} - {r.tipo_cucina}")
        elif scelta == "2":
            nome = input("Inserisci il nome del ristorante: ")
            tipo_cucina = input("Inserisci il tipo di cucina: ")
            descrizione = input("Inserisci una breve descrizione del ristorante: ")
            nuovo_ristorante = Ristorante(nome, tipo_cucina, descrizione)
            ristoranti.append(nuovo_ristorante)
            print(f"Ristorante {nome} aggiunto con successo.")
        elif scelta == "3":
            if len(ristoranti) == 0:
                print("Non ci sono ristoranti disponibili da gestire.")
            else:
                for i, r in enumerate(ristoranti):
                    print(f"{i}: {r.nome} - {r.tipo_cucina}")
                indice = int(input("Inserisci l'indice del ristorante da gestire: "))
                if 0 <= indice < len(ristoranti):
                    gestisci_ristorante(ristoranti[indice])
                else:
                    print("Indice non valido.")
        elif scelta == "4":
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida. Riprova.")

gestisci_ristoranti()
