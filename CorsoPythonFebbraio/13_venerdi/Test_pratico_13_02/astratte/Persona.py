from implementazioni.Accesso import Accesso
from abc import ABC, abstractmethod


# Astrazione della classe
class Persona(ABC):

    def __init__(self, nome: str, cognome: str):
        # incapsulamento, utilizzo di variabili protette
        self._nome = nome
        self._cognome = cognome

    def nome_completo(self) -> str:
        # incapsulamento, utilizzo di metodi per accedere alle variabili protette
        return f"{self._nome} {self._cognome}"
    
    @abstractmethod
    def get_accesso(self) -> Accesso:
        # polimorfismo, tutte le sotto classi devono implementare questo metodo
        # restituendo il ruolo
        # esempio developer, ai developer
        pass