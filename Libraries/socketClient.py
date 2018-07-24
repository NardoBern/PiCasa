import socket
class ethernet_connection:

    def inizializzazione(self):
        #global sock,TCP_IP,TCP_PORT,BUFFER_SIZE
        self.TCP_IP = '127.0.0.1' #INDIRIZZO IP DEL SERVER
        self.TCP_PORT = 1001 #PORTA TCP CONNESSIONE AL SERVER
        self.BUFFER_SIZE = 1024 #DIMENSIONE BUFFER DI RICEZIONE RISPOSTA DAL SERVER
        self.sock = None #INIZIALIZZAZIONE SOCKET

    def connessione(self):
        #SE NON SONO ANCORA CONNESSO, ALLORA LANCIO LA CONNESSIONE

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #CREO IL SOCKET
        	#print sock
        self.sock.settimeout(0.3) #TIMEOUT DI CONNESSIONE A 300msec.
        try:
            self.sock.connect((self.TCP_IP,self.TCP_PORT)) #LANCIO LA CONNESSIONE
        except socket.timeout,e:
            print 'TIMEOUT DI CONNESSIONE' #SE ENTRO I 300ms LA CONNESSIONE FALLISCE VADO IN TIMEOUT
            self.sock.close
            self.sock = None
                        #continue
        except socket.error,e:
            print 'ERRORE DI CONNESSIONE ', e
            self.sock.close
            self.sock = None
                        #continue
    def disconnessione(self):
        #SE SONO CONNESSO MI DISCONNETTO

        if self.sock != None:
            try:
                self.sock.close
                self.sock = None
            except socket.error, e:
                print 'ERRORE DI DISCONNESSIONE', e
                self.sock.close
                self.sock = None
                #continue
    def invio_dati(self,dati):
        #FUNZIONE DI INVIO DEI DATI (dati deve essere di tipo STRING o BUFFER)

        if self.sock == None :
            print 'NESSUNA CONNESSIONE AL SERVER, PROVO A CONNETTERMI'
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #CREO IL SOCKET
        	#print sock
            self.sock.settimeout(0.3) #TIMEOUT DI CONNESSIONE A 300msec.
            try:
                self.sock.connect((self.TCP_IP,self.TCP_PORT)) #LANCIO LA CONNESSIONE
            except socket.timeout,e:
                print 'TIMEOUT DI CONNESSIONE' #SE ENTRO I 300ms LA CONNESSIONE FALLISCE VADO IN TIMEOUT
                self.sock.close
                self.sock = None
                #continue
            except socket.error,e:
                print 'ERRORE DI CONNESSIONE ', e
                self.sock.close
                self.sock = None
        else:
            try:
                self.sock.send(dati)
            except socket.error, e:
                print 'ERRORE NEL INVIO DEI DATI', e
                self.sock.close
                self.sock = None
                #continue
    def ricezione_dati(self):
        #FUNZIONE DI RICEZIONE DATI
        #IMPOSTO IL TIMEOUT DI CONNESSIONE A 200 ms
        if self.sock != None:
            self.sock.settimeout(0.2)
            try:
                dati_ricevuti = self.sock.recv(self.BUFFER_SIZE)
                return dati_ricevuti
            except self.socket.timeout, e:
                err = e.args[0]
                if err == 'timed out':
                    print 'NESSUNA RISPOSTA RICEVUTA'
                    #continue
                else:
                    print e
                    sys.exit(1)
