# polimorfismo passivo

si basa sul concetto di duck typing.
Non è necessario che un coggetto appartenga a una gerarchia di classi specifica


basta che l'oggetto si comporti come ci sia spetta
    - ovvero che abbia i metodi uguali ad altre classi
    - permette di avere polimorfismo senza avere una gerarchia


# astrazione
a livello pratico la capacità di dividere gli elementi nascosti di basso livello, dalle implementazione reali
nasconde dettagli complessi (con una certa logica) attraverso una chiamata semplice

COSA (strazione)
il programmatore che usa una funzione può non si preoccupa di come funziona

COME il come non ci interessa

# classi astratte
- classi astratte
- metodi astratti

- sono usate come modello per altre classi
- non possono essere istanziate


impone un'interfaccia comune tra classi diverse che obbligano l'implementazione di determinati metodi

- può avere metodi reali e variabili ma non può essere istanziata