from astratte.Persona import Persona
from implementazioni.Badge import Badge


# ereditarietà, eredita dalla classe astratta Persona metodi (da implementare) e attributi 
class Dipendente(Persona):

    def __init__(self, nome: str, cognome: str, badge: Badge, ruolo: str):
        super().__init__(nome, cognome) # chiamata al costruttore della classe padre (Persona)
        # init delle variabili private per la classe Dipenedente
        self.__badge = badge
        self.__ruolo = ruolo

    # polimorfismo metodo con comportamento specifico per la classe Dipendente
    def get_ruolo(self) -> str:

        pass
    
    # polimorfismo metodo con comportamento specifico per la classe Dipendente 
    def accedi_lavoro(self) -> bool:

        pass