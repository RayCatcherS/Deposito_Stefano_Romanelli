from implementazioni.Accesso import Accesso
from astratte.Persona import Persona


# ereditarietà, eredita dalla classe astratta Persona metodi (da implementare) e attributi 
class Visitatore(Persona):

    def __init__(self, nome: str, cognome: str):
        super().__init__(nome, cognome) # chiamata al costruttore della classe padre (Persona)

    # polimorfismo metodo con comportamento specifico per la classe Dipendente
    def get_accesso(self) -> Accesso:

        accesso = Accesso(badge=None, ruolo="Visitatore")
        return accesso
    