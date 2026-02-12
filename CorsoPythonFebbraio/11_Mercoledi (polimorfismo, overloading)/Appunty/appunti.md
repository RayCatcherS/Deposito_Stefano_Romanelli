# incapsulamento

### protezione attributi
- attributi privati: con doppio undescore __attributo
        non modificabile dall'esterno dalla classe 
        non viene ereditato, è privato alla classe padre

- attributi protetti: con unico undescore _attributo
        protetto => utilizzabile solo nella classe ed ereditabile nelle sottoclassi

- metodi (getter, setter)
    servono ad ottenere accesso all'accesso e alla modifica dei dati



compilatore blocca gli accessi in fase di compilazione
- su private

invece su protected è una convenzione ed è visibile ai figli


## scope
- globale: variabile dichiarata fuori da tutte le funzioni è vista globalmente
    accessibile da ogni punto del codice

- locale: dichiarate all'interno di funzione (quelle locali sovrascrivono le globali)

- non-locale nelle funzioni annidate (varibile accessibile in più di una funzione interna)
    funzione
        z = 10
        funzione
            nonlocal z # permette di accedere alla variabile superiore (senza sarebbe uno scope interno)
            z = 10


# polimorfismo
metodi polimorfici (sul tipo di dato)
funzione che tratta quel dato come il tipo più generico possibile


# overload non esiste si può simulare
(meccanismo basato sui parametri)è possibile simulare l'overloading utilizzando argomenti opzionali o variadici


