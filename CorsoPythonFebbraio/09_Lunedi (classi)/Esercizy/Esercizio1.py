
class Punto:
    x, y = 0.0, 0.0
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):
        # distanza tra il punto e l'origine (0,0)
        return (self.x**2 + self.y**2)**0.5


def inserimento_punti():
    while True:
        x = float(input("Inserisci coordinata x: "))
        y = float(input("Inserisci coordinata y: "))
        punto = Punto(x, y)
        punti.append(punto)

        scelta = input("Vuoi inserire un altro punto? (s/n) ")
        if scelta.lower() != 's':
            break

def muovi_punto(punto):
    dx = float(input("Inserisci spostamento in x: "))
    dy = float(input("Inserisci spostamento in y: "))
    punto.muovi(dx, dy)
    print(f"Il punto si trova ora in ({punto.x}, {punto.y})")
    print(f"Distanza dall'origine: {punto.distanza_da_origine()}")

def selezione_punto(punti: list):
    resultato = None
    print("Punti disponibili:")
    if(len(punti) == 0):
        print("Nessun punto disponibile.")
        resultato = None
    for i, punto in enumerate(punti):
        print(f"{i}: ({punto.x}, {punto.y})")
    indice = int(input("Seleziona un punto (inserisci l'indice): "))
    if 0 <= indice < len(punti):
        resultato = punti[indice]
    else:
        print("Indice non valido.")
        resultato = None
    return resultato

def visualizza_punti(punti: list):
    if(len(punti) == 0):
        print("Nessun punto disponibile.")
    else:
        for i, punto in enumerate(punti):
            print(f"{i}: ({punto.x}, {punto.y})")

punti = []
while True:
    scelta_main = input("seleziona un'opzione: 1 crea punti, 2 muovi punto, 4 visualizza punti, 3 esci: ")
    if(scelta_main == "1"):
        inserimento_punti()
    elif(scelta_main == "2"):
        punto = selezione_punto(punti)
        if punto == None:
            print("Nessun punto selezionato.")
        else:
            muovi_punto(punto)

    elif(scelta_main == "4"):
        if(len(punti) == 0):
            print("Nessun punto disponibile.")
        else:
            visualizza_punti(punti)
    elif(scelta_main == "3"):
        break