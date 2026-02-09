USER_ROLE = "cliente"
ADMIN_ROLE = "admin"
class Negozio:
    nome = None
    articoli = None
    utenti = None
    def __init__(self, nome:str, utenti:dict, articoli:dict):
        self.nome = nome
        self.utenti = utenti
        self.articoli = articoli
        
    # restituisce l'utente se le credenziali sono corrette, altrimenti restituisce None
    def login(self, uid=None):
            if uid in self.utenti:
                print(f"Benvenuto {self.utenti[uid]['nome']}!")
                return self.utenti[uid]
            else:
                print("ID utente non valido. Riprova.")

def visualizzaNegozi():
    # stama i negozi disponibili con indice
    print("Negozi disponibili:")
    for i, negozio in enumerate(negozio):
        print(f"{i}: Negozio con {len(negozio.utenti)} utenti e {len(negozio.articoli)} articoli.")   

def selezionaNegozio(negozi: list):
    while True:
        indice = int(input("Seleziona il negozio a cui vuoi accedere (inserisci l'indice): "))
        if 0 <= indice < len(negozi):
            return negozi[indice]
        else:
            print("Indice non valido. Riprova.")

def accediNegozio(utente: dict, negozio: Negozio):
    print(utente)
    '''
    while True:
        input_azione = input("Cosa vuoi fare? 1 visualizza articoli, 2 seleziona e acquista articoli, 3 esci: ")

        if input_azione == "1":
            print(f"Articoli disponibili nel negozio {negozio.nome}:")
            for id_articolo, articolo in negozio.articoli.items():
                print(f"{id_articolo}: {articolo['nome']} - {articolo['prezzo']}€")
    '''

negozi = [
    Negozio(
        "Negozio di abbigliamento",
        {
            1: {"nome": "Mario", "ruolo": USER_ROLE},
            2: {"nome": "Luigi", "ruolo": USER_ROLE},
            3: {"nome": "Admin", "ruolo": ADMIN_ROLE},
        },
        {
            1: {"nome": "Pantaloni", "prezzo": 50},
            2: {"nome": "Maglietta", "prezzo": 20},
            3: {"nome": "Scarpe", "prezzo": 100},
        }
    )
]
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
                    accediNegozio(uid, negozio_scelto)
                    break
                else:
                    print("ID utente non valido per il negozio. Riprova.")
                riprova = input("Riprovare? (s/n): ")
                if riprova.lower() != "s":
                    break
        elif scelta == "2":
            print("Arrivederci!")
            break

main()