from implementazioni.Azienda import Azienda
from implementazioni.Dipendente import Dipendente
from implementazioni.Visitatore import Visitatore
from implementazioni.Badge import Badge


def main():
    azienda = Azienda({1, 2, 3}) 
    visitatore = Visitatore("Mario", "Rossi")
    dipendente1 = Dipendente("Luigi", "Verdi", Badge(1, "Developer"))
    dipendente2 = Dipendente("Giovanni", "borghi", Badge(2, "Manager"))
    dipendente3 = Dipendente("Paolo", "gialli", Badge(5, "AI developer"))


    azienda.esegui_accesso(visitatore.get_accesso())
    azienda.esegui_accesso(dipendente1.get_accesso())
    azienda.esegui_accesso(dipendente2.get_accesso())
    azienda.esegui_accesso(dipendente3.get_accesso())


main()