# Analisi dei dati

### pip (python install package)
pip è il sistema di gestione dei pacchetti usato da python usato per installare e gestire pacchetti software

installare dipendenze facilmente da PyPI (python package index), è un repository 


- **pip install nomepacchetto** : permette di installare pacchetti da PyPI, github e altre fonti che supportano il formato distribuzione pacchetti python. 
specificando la versione desiderata o l'ultima (se non specificata)

- **Gestione delle dipendenze** : pip risolve tutte le dipendenze automaticamente se questa lib necessita altre librerie

- **Aggiornamento e rimozione pacchetti** : 

- **Gestione versioni** : supporta installazione di versioni specifiche dei pacchetti, gestendo upgrade e downgrade tra le dipendenze

- **Integrazione con ambienti virtuali** : PIP funziona bene con ambienti virtuali come venv o virtual venv, permettendo agli sviluppatori di avere un ambiente isolato per ogni progetto


## NumPy 
- Libreria fondamentale per il calcolo scientifico in python

- supporto per operazioni vettoriali (sono inutili i cicli per agire sugli array)

- fornisce supporto per array e matrici multidimensionali

- funzioni matematiche per operare sugli array

Usato intensivamente nell'analisi dei dati


## Configurazione di NumPy

Usare gestore pacchetti pip:

```
pip install numpy
```

importare NumPy nel tuo script Python:

```
import numpy as np
```
np alias convenzionale

### cosa è
è una libreria open-source:

- supporta array multidimensionali (ndarray) più efficienti in termini di memoria e prestazioni rispetto alle liste native python
- funzioni matetiche per operare sugli array (op vettoriali e matriciali). Algebra lineare, trasformate di fourier, funzioni statistiche
- strumenti per integrare codice C/C++ e Fortran per ottimizzare ulteriormente le prestazioni delle operazioni


### Keyword Numpy
- **ndarray**: array multidimensionale (n-dimensionali), veloci ed efficienti
- **dtype** specifica il tipo di dato negli array (int, float, bool, etc..)
- **shape**: restituisce dimensione dell'array (es (3,4) per un array bidimensionale). Viene preso il max
- **arange**: funzione per creare array con valori sequenziali. Similari a range ma per array (invece della lista)
- **reshape**: modifica lo shape dell'array senza modificare i suoi valori
- **linspace**: crea un array di numeri distribuiti uniformemente tra due estremi.
- **random**: genera array con valori casuali con distribuzioni normali o uniforme
- **sum, meand, std**: funzioni per calcolare somma, media e deviazione standard su elemnti di array