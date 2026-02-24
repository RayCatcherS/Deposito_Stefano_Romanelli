# operazioni

vettoriale: applicata a tutti i valori

universali: restituisce un valore come la media dell'intero vettore

## funzioni matematiche e statistiche


## broadcasting
Broadcasting

Il broadcasting è una potente funzione
di NumPy che permette di eseguire
operazioni aritmetiche
forme diverse.

Questo riduce la necessità di creare array
compatibili per le operazioni.


Il broadcasting rende più semplice e veloce la scrittura di codice per
operazioni element-wise.

**Principi del Broadcasting**
. Allineamento delle Dimensioni:
o Quando NumPy esegue operazioni su due array, verifica se le loro
dimensioni sono compatibili. Due dimensioni sono compatibili se:
. Sono uguali.
. Una delle due dimensioni è 1.

**Espansione delle Dimensioni:**
sono
le dimensioni non
dimensioni di uno degli array automaticamente. L'array con la
dimensione 1 viene espanso per avere la stessa dimensione
dell'altro array.

**Applicazione dell'Operazione:**
o Una volta che gli array hanno dimensioni compatibili, NumPy
esegue l'operazione element-wise. L'array più piccolo viene
replicato per riempire l'array più grande.


**vantaggi broadcasting**
- evita di creare copie di array per eseguire le operazioni
- rende più semplice il richiamo di funzioni

regole bradcasting
l'array con meno dimensione 

gli array vanno allineati con a sinistra i più complessi a destra quelli meno

espansione automatica delle dimensioni
se una delle dimensioni è 1, viene espansa per avere la stessa dimensione dell'altro array.
