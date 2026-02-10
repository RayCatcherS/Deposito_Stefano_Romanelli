import EsercizioClassy


def main():
    magazzino = EsercizioClassy.Magazzino()

    for i in range(5):
        magazzino.aggiungi_pacco()

    # spedisci 2 pacchi
    magazzino.gestore_pacchi.spedisci_pacco(magazzino.cerca_pacco("0"))
    magazzino.gestore_pacchi.spedisci_pacco(magazzino.cerca_pacco("1"))

    # consegna 1 pacco
    magazzino.gestore_pacchi.consegna_pacco(magazzino.cerca_pacco("0"))

    # mostra in magazzino
    magazzino.mostra_pacchi_per_stato(EsercizioClassy.IN_MAGAZZINO)

    # mostra in consegna
    magazzino.mostra_pacchi_per_stato(EsercizioClassy.IN_CONSEGNA)

    # somma peso totale pacchi non consegnati
    somma_peso_non_consegnati = magazzino.gestore_pacchi.calcola_peso_tot(magazzino.filtra_pacchi_per_stato(EsercizioClassy.IN_MAGAZZINO))
    print("Peso totale pacchi non consegnati:", somma_peso_non_consegnati)

    # visualizza pacchi consegnati
    print("Pacchi spediti e consegnati:")
    magazzino.mostra_pacchi_per_stato({EsercizioClassy.CONSEGNATO, EsercizioClassy.IN_CONSEGNA})

main()