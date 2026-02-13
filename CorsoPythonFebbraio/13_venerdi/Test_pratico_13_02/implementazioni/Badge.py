# Incapsulamento: il badge sarà incapsulato in modo che non possa essere modificato direttamente
class Badge:
    def __init__(self, codice: str):
        self.__codice = codice          # Private attribute