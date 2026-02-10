# classe base
class Animale:
    def __init__(self, nome):
        self.nome = nome
    
    def parla(self):
        print(f"{self.nome} fa suono generico.")



# classe derivata 
class Cane(Animale):
    def parla(self):
        print(f"{self.nome} abbaia")


animale_generico = Animale("Animale generico")

cane = Cane("Fido")

animale_generico.parla()
cane.parla()