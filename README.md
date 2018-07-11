# PiCasa
Raspberry pi home management

## Generalità

Il software di gestione della domotica di casa viene suddiviso in moduli, in funzione delle utilities che devono essere gestite.
Vi sarà un modulo definito _coordinatore_ che si interfaccierà con i database _data_store_ e _data_commands_, per presentare lo stato dell'impianto e ricevere i comandi dall'interfaccia operatore.
Il modulo si interfaccierà inoltre con i restanti moduli di impianto (es.: _moduloLuci_) che gestiranno le singole tipologie di utenze. L'interfacciamento sarà attraverso una connessione server-client tramite socket TCP/IP. Il protocollo utilizzato è descritto qui sotto.
I vari moduli risiederanno su file differenti, saranno eseguibili indipendenti che potranno essere lanciati singolarmente.
Inoltre potranno godere di _vita propria_, ossia funzionare indipendentemente dagli altri, compreso dal _modulo coordinatore_.
Vi sarà una libreria comune.

## Protocollo di comunicazione _intermodulare_ socket TCP/IP
I vari moduli risiederanno sullo stesso device (raspberry pi). La comunicazione avverrà quindi con indirizzo IP localhost e i vari moduli avranno una loro porta dedicata.
Il modulo _coordinatore_ agirà da _client_, mentre i _moduli utenza_ saranno dei _server_.
I comandi ed i feedback verranno inviati attraverso lo scambio di una variabile di tipo intero.

### Richiesta di vita
Codice di richiesta: 990 (sei vivo?)
Codice di risposta dal modulo: 999 (si, sono vivo)

### Invio dati da _coordinatore_ a _modulo_
Codice di invio: 100 + dati
Codice di risposta dal modulo: 199 (dati ricevuti)

### Lettura dati da _coordinatore_ a _modulo_
Codice di invio: 200
Codice di risposta dal modulo: 299 + dati.

_N.B.: il dettaglio dello scambio dati verrà definito per ciasun modulo. Ciò che si può definire a questo punto dello sviluppo è che ogni comunicazione dovrà iniziare con una "richiesta di vita", dopodichè si avrà l'invio dei codici di richiesta successivi._
