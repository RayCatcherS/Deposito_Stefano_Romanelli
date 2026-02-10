import datetime


USER_ROLE = "cliente"
ADMIN_ROLE = "admin"
class Negozio:
    nome = None
    articoli = None
    utenti = None
    acquisti = []
    def __init__(self, nome:str, utenti:dict, articoli:dict):
        self.nome = nome
        self.utenti = utenti
        self.articoli = articoli
    
    def visualizza_utenti(self):
        print(f"Utenti registrati nel negozio {self.nome}:")
        for id_utente, utente in self.utenti.items():
            print(f"{id_utente}: {utente['nome']} - Ruolo: {utente['ruolo']}")

    def nuovo_amministratore(self):
        # calcola id utente (progressione numerica) codice semplice
        id_utente = max(self.utenti.keys()) + 1 if self.utenti else 1 # se il dizionario è vuoto, inizia da 1, altrimenti prendi il massimo id esistente e aggiungi 1
        nome_utente = input("Inserisci il nome del nuovo utente: ")
        ruolo_utente = ADMIN_ROLE
        self.utenti[id_utente] = {
            "nome": nome_utente,
            "ruolo": ruolo_utente,
            "id": id_utente
        }

    # restituisce il guadagno totale 
    def guadagnaTot(self):
        return sum(acquisto["articolo"]["prezzo"] for acquisto in self.acquisti)

    # restituisce l'utente se le credenziali sono corrette, altrimenti restituisce None
    def login(self, uid=None):
            if uid in self.utenti:
                print(f"Benvenuto {self.utenti[uid]['nome']}!")
                return self.utenti[uid]
            else:
                print("ID utente non valido. Riprova.")

    # comportamento del cliente
    def __user_access_behavior(self, utente: dict):
        while True:
            input_azione = input("Cosa vuoi fare? 1 visualizza articoli, 2 seleziona e acquista articoli, 3 esci: ")

            if input_azione == "1":
                self.visualizza_articoli()
            elif input_azione == "2":
                while True:
                    self.visualizza_articoli()
                    id_articolo_input = int(input("Inserisci l'ID dell'articolo che vuoi acquistare: "))
                    if id_articolo_input in self.articoli:
                        self.acquista(utente["id"], id_articolo_input)
                        break
                    else:
                        print("ID articolo non valido. Riprova.")
            elif input_azione == "3":
                print("Uscita dal negozio.")
                break
    
    # comportamento dell'amministratore
    def __admin_access_behavior(self, utente: dict):
        while True:
            input_azione = input("Cosa vuoi fare? 1 visualizza articoli, 2 aggiungi articolo, 3 rimuovi articolo, 4 modifica articolo, 5 rapporto vendite, 6 visualizza guadagni tot, 7 inserisci amministratore, 8 visualizza utenti, 9 esci: ")
            if input_azione == "1":
                self.visualizza_articoli()
            elif input_azione == "2":
                self.aggiungi_articolo()
            elif input_azione == "3":
                self.rimuoviArticolo()
            elif input_azione == "4":
                self.modificaArticolo()
            elif input_azione == "5":
                self.rapportoVendite()
            elif input_azione == "6":
                tot = self.guadagnaTot()
                print(f"Guadagno totale: {tot}€")
            elif input_azione == "7":
                self.nuovo_amministratore()
            elif input_azione == "8":
                self.visualizza_utenti()
            elif input_azione == "9":
                print("Uscita dal negozio.")
                break
            else:
                print("Azione non valida. Riprova.")
    
    # metodo per aggiungere un articolo al dizionario degli articoli con un id univoco
    def aggiungi_articolo(self):
        while True:
            nome_articolo = input("Inserisci il nome dell'articolo: ")
            prezzo_articolo = float(input("Inserisci il prezzo dell'articolo: "))
            quantità_articolo = int(input("Inserisci la quantità dell'articolo: "))
            id_articolo = max(self.articoli.keys()) + 1 if self.articoli else 1
            self.articoli[id_articolo] = {
                "nome": nome_articolo,
                "prezzo": prezzo_articolo,
                "quantità": quantità_articolo
            }
            print(f"Articolo '{nome_articolo}' aggiunto con ID {id_articolo}.")
            if input("Vuoi aggiungere un altro articolo? (s/n): ").lower() != "s":
                break
    
    # metodo per visualizzare gli articoli disponibili, stampa nome, prezzo e quantità disponibile
    def visualizza_articoli(self):
        print(f"Articoli disponibili nel negozio {self.nome}:")
        for id_articolo, articolo in self.articoli.items():
            print(f"{id_articolo}: {articolo['nome']} - {articolo['prezzo']}€ - {articolo['quantità']} disponibili")

    # metodo per rimuovere un articolo, chiede l'id dell'articolo da rimuovere e lo rimuove dal dizionario degli articoli
    def rimuoviArticolo(self):
        while True:
            id_articolo_input = int(input("Inserisci l'ID dell'articolo da rimuovere: "))
            if id_articolo_input in self.articoli:
                articolo_rimosso = self.articoli.pop(id_articolo_input)
                print(f"Articolo '{articolo_rimosso['nome']}' con ID {id_articolo_input} rimosso.")
                break
            else:
                print("ID articolo non valido. Riprova.")
            if input("Vuoi rimuovere un altro articolo? (s/n): ").lower() != "s":
                break
    
    # metodo per modificare un articolo, permette di modificare nome, prezzo e quantità
    def modificaArticolo(self):
        while True:
            id_articolo_input = int(input("Inserisci l'ID dell'articolo da modificare: "))
            if id_articolo_input in self.articoli:
                articolo = self.articoli[id_articolo_input]
                print(f"Articolo selezionato: {articolo['nome']} - {articolo['prezzo']}€ - {articolo['quantità']} disponibili")
                nuovo_nome = input("Inserisci il nuovo nome dell'articolo (lascia vuoto per mantenere quello attuale): ")
                nuovo_prezzo = input("Inserisci il nuovo prezzo dell'articolo (lascia vuoto per mantenere quello attuale): ")
                nuova_quantità = input("Inserisci la nuova quantità dell'articolo (lascia vuoto per mantenere quella attuale): ")

                if nuovo_nome:
                    articolo["nome"] = nuovo_nome
                if nuovo_prezzo:
                    articolo["prezzo"] = float(nuovo_prezzo)
                if nuova_quantità:
                    articolo["quantità"] = int(nuova_quantità)

                print(f"Articolo con ID {id_articolo_input} modificato: {articolo['nome']} - {articolo['prezzo']}€ - {articolo['quantità']} disponibili")
                break
            else:
                print("ID articolo non valido. Riprova.")
            if input("Vuoi modificare un altro articolo? (s/n): ").lower() != "s":
                break
    
    # metodo per effettuare un acquisto, verifica che l'utente sia autenticato e che l'articolo sia disponibile
    def acquista(self, uid, id_articolo):
        if uid not in self.utenti:
            print("Utente non autenticato. Acquisto negato.")
            return
        if id_articolo not in self.articoli:
            print("Articolo non disponibile. Acquisto negato.")
            return
        
        articolo = self.articoli[id_articolo]
        print(f"Acquisto effettuato: {articolo['nome']} per {articolo['prezzo']}€ da parte di {self.utenti[uid]['nome']}.")
        # Aggiungi l'acquisto alla cronologia degli acquisti dell'utente
        self.acquisti.append({
            "utente": self.utenti[uid],
            "articolo": articolo,
            "data": datetime.date.today().isoformat()
        })
    
    # metodo per visualizzare il rapporto vendite con data, nome utente, articolo acquistato e prezzo
    def rapportoVendite(self):
        print("Rapporto vendite:")
        for acquisto in self.acquisti:
            print(f"{acquisto['data']}: {acquisto['utente']['nome']} ha acquistato {acquisto['articolo']['nome']} per {acquisto['articolo']['prezzo']}€")

    # metodo per accedere al negozio, verifica il ruolo dell'utente e chiama il comportamento corrispondente al ruolo
    def accediNegozio(self, utente: dict):
        print(f"Accesso al negozio {self.nome}...")
        if utente is None:
            print("Accesso negato. Utente non autenticato.")
            return
        print(f"Benvenuto {utente['nome']}! Ruolo: {utente['ruolo']}")
    
        if utente["ruolo"] == USER_ROLE:
            self.__user_access_behavior(utente)

        elif utente["ruolo"] == ADMIN_ROLE:
            self.__admin_access_behavior(utente)
        else:
            print("Ruolo utente non riconosciuto. Accesso limitato.")

        print(utente)


def visualizzaNegozi():
    # stama i negozi disponibili con indice
    print("Negozi disponibili:")
    for i, negozio in enumerate(negozi):
        print(f"{i}: Negozio con {len(negozio.utenti)} utenti e {len(negozio.articoli)} articoli.")   

def selezionaNegozio(negozi: list):
    while True:
        indice = int(input("Seleziona il negozio a cui vuoi accedere (inserisci l'indice): "))
        if 0 <= indice < len(negozi):
            return negozi[indice]
        else:
            print("Indice non valido. Riprova.")



def main():
    print("Benvenuto nel negozio!")
    
    while True:
        uid = None
        scelta = input("cosa vuoi fare? 1 login ad un negozio, 2 esci: ")

        if scelta == "1":
            visualizzaNegozi()
            negozio_scelto = selezionaNegozio(negozi)

            while True:
                uid_user_input = int(input("Inserisci il tuo ID utente: "))
                uid = negozio_scelto.login(uid_user_input)
                if uid is not None:
                    print(f"Utente {uid['nome']} con ruolo {uid['ruolo']} ha effettuato il login al negozio {negozio_scelto.nome}.")
                    negozio_scelto.accediNegozio(uid)
                    break
                else:
                    print("ID utente non valido per il negozio. Riprova.")
                riprova = input("Riprovare? (s/n): ")
                if riprova.lower() != "s":
                    break
        elif scelta == "2":
            print("Arrivederci!")
            break

negozi = [
    Negozio(
        "Negozio di abbigliamento",
        {
            1: {"nome": "Mario", "ruolo": USER_ROLE, "id": 1},
            2: {"nome": "Luigi", "ruolo": USER_ROLE, "id": 2},
            3: {"nome": "Admin", "ruolo": ADMIN_ROLE, "id": 3},
        },
        {
            1: {"nome": "Pantaloni", "prezzo": 50, "quantità": 10, "id": 1},
            2: {"nome": "Maglietta", "prezzo": 20, "quantità": 20, "id": 2},
            3: {"nome": "Scarpe", "prezzo": 100, "quantità": 5, "id": 3},
        }
    )
]
main()