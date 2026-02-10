
class Prodotto():
    def __init__(self, nome:str, costo_produzione: int, prezzo_vendita:int):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
    
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

class Elettronica(Prodotto):
    def __init__(self, nome:str, costo_produzione: int, prezzo_vendita:int, garanzia:int,):
        Prodotto.__init__(self, nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia

class Abbigliamento(Prodotto):
    def __init__(self, nome:str, costo_produzione: int, prezzo_vendita:int, materiale:str):
        Prodotto.__init__(self, nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale

class Fabbrica():
    profitto: float = 0.0
    prodotti = []
    inventario = {}
    def __init__(self):
        pass
    # codice pacco incrementale
    def calcola_codice__nuovo_prodotto(self):
        if len(self.prodotti) == 0:
            return "0"
        else:
            return str(len(self.prodotti)+ 1) 
        
    def aggiungi_prodotto(self, prodotto: Prodotto):

        # aggiorna inventario e prodotti
        if prodotto.nome in self.inventario.keys():
            self.inventario[prodotto.nome] = self.inventario[prodotto.nome] + 1
        else:
            self.prodotti.append(prodotto)
            self.inventario[prodotto.nome] = 1

    def visualizza_prodotti(self):
        for i, prod in enumerate(self.prodotti):
            print(f"{i} - {prod.nome}")

    def visualizza_inventario(self):
        for chiave, valore in self.inventario.items():
            print(f"{chiave}: {valore}")

    def vendi_prodotto(self, p_name: str):
        if p_name in self.inventario.keys():

            if self.inventario[p_name] == 0:
                print("prodotto esaurito")
            elif self.inventario[p_name] > 0:

                # aggiorna inventario
                self.inventario[p_name] = self.inventario[p_name] - 1

                # aggiorna prezzo vendita
                for prodotto in self.prodotti:
                    if prodotto.nome == p_name:
                        self.profitto = self.profitto + prodotto.prezzo_vendita
                        break
                
                
            else:
                print("errore")
        else:
            print("il prodotto non è presente")
    
    def resi_prodotto(self, p_name):
        if p_name in self.inventario.keys():

            # aggiorna inventario
            self.inventario[p_name] = self.inventario[p_name] + 1
        else:
            print("il prodotto non è presente")

    def visualizza_profitto(self):
        print(self.profitto)

def main():
    fabbrica = Fabbrica()
    prodotti = [
        Elettronica("televisore", 200, 500, 2),
        Elettronica("cell", 50, 200, 2),
        Abbigliamento("jeans", 10, 49, "cotone")
    ]

    for prod in prodotti:
        fabbrica.aggiungi_prodotto(prod)

    fabbrica.aggiungi_prodotto(Elettronica("cell", 50, 200, 2))
    fabbrica.resi_prodotto("jeans")
    fabbrica.resi_prodotto("jeans")
    fabbrica.resi_prodotto("jeans")
    fabbrica.visualizza_inventario()

    fabbrica.visualizza_prodotti()


    fabbrica.vendi_prodotto("jeans")

    fabbrica.visualizza_profitto()
main()