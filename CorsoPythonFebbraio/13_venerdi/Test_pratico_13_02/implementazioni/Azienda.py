from implementazioni.Accesso import Accesso

class Azienda:
    
    

    def __init__(self, id_dipendenti):
        self.__dipendenti = id_dipendenti 
        pass
    
    def esegui_accesso(self, accesso: Accesso):
        if accesso.get_ruolo() == "Visitatore":
            print(f"Benvenuto {accesso.get_ruolo()}")
        
        # Se ha un badge, allora è un dipendente
        elif accesso.get_badge() is not None: 
            if accesso.get_badge().get_id() in self.__dipendenti:
                print(f"Accesso Dipendente {accesso.get_badge().get_id()} ({accesso.get_ruolo()}) consentito")
            else:
                print(f"Accesso Dipendente {accesso.get_badge().get_id()} negato: ID non autorizzato")
        
        else: 
            print("Errore: Accesso non riconosciuto")