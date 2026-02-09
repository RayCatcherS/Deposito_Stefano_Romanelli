# Classi python
- le classi permette di creare nuovi tipi di dati
- sono un modello di riferimento per la creazione di oggetti


### astrazione
- le classi sono astrazione di concetti del mondo reale


### come sono fatte
le classi contengono
- metodi 
- metodi speciali (costruttori)
- attributi
- altre classi

### oggetto
l'oggetto è un'istanza della classe, con avvaloramento delle sue proprietà


# esposizione parametri


### i metodi
- sono funzioni associate alla classe
- i metodi rappresentano i comportamenti degli oggetti
- i metodi speciali sono quelli che iniziano e finiscono con __ (es. __init__ è il costruttore)

ESEMPIO: 

class Automobile:                                           # dichiaro la classe (lettera maiuscola)
    numero_di_ruote = 4                                     # attributo di classe
    def __init__(self, marca, modello):                     # metodo costruttore
        self.marca = marca                                  # attributo di istanza
        self.modello = modello                              # attributo di istanza  

    def stampa_info(self):                                  # metodo di istanza
        print("L'automobile è una", self.marca, self.modello)



### Costruttore
- è un metodo speciale che viene chiamato quando si crea un oggetto della classe
il costruttore non è obbligatorio 
- serve ad inizializzare l'oggetto istanziato
- self è obbligatorio, rappresenta l'oggetto stesso (esponenendo i suoi attributi e metodi)
- il self non accetta valori, è un riferimento all'oggetto stesso

class Person():
    pass
persona1 = Person()                                        # creo un oggetto della classe Person

oppure 

class Person():
    x = 10
    def __init__(self):                       # costruttore con parametri
        pass                                  # attributo di istanza

persona2 = Person()                                       

                                        

### modifica valori oggetti
è possibile modificare gli attributi di istanza anche dopo la creazione dell'oggetto 
persona2.x = 20     

modifica valori di classe
- è possibile modificare gli attributi di classe, ma questa modifica influenzerà tutti gli oggetti della classe
Person.x = 30      # modifica l'attributo di classe x, influenzando tutti gli oggetti della classe Person



### Metodi di classe
- metodi statici (non lavorano con i singoli(istanze) e neanche con con la classe vengono definiti con @staticmethod e non accettano come primo parametro né self né cls)
- metodi di classe (non lavorano con i singoli(istanze) oggetti ma sulla classe vengono definiti con @classmethod e accettano come primo parametro cls, che rappresenta la classe stessa)
- metodi di istanza (vengono definiti e chiamati con l'oggetto)

### metodo statico
- Serve a raggruppare logicamente funzionalità che non dipendono né dall'istanza né dalla classe, non accettano come primo parametro né self né cls.

### metodo di classe
- Serve a raggruppare funzionalità che operano sulla classe stessa, accettano come primo parametro cls, che rappresenta la classe stessa. Usa @classmethod per definirlo.

### metodo di istanza
- Serve a definire comportamenti specifici per ogni istanza della classe, accettano come primo parametro self, che rappresenta l'istanza stessa. Viene definito senza decoratori speciali.


# Dizionari
- sono strutture (oggetti) dati che memorizzano coppie chiave-valore
- sono mutabili, ordinata
- sono delimitati da parentesi graffe {}
- tipo di dato dict 
ESEMPIO:
dizionario = {"chiave1": "valore1", "chiave2":
"valore2"}
dizionario["chiave1"]     # restituisce "valore1"
- le chiavi devono essere univoche e immutabili (es. stringhe, numeri, tuple)
- i valori possono essere di qualsiasi tipo


- sono utili per rappresentare oggetti e tabelle di dati (valori)

## metodi e funzioni per i dizionari
Sono presenti nel file Dizionatri.py