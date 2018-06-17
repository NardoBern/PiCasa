import socket
class ethernet_connection:
    sock = None
    def inizializzazione(self):
        global sock,TCP_IP,TCP_PORT,BUFFER_SIZE
        TCP_IP = '192.168.2.15' #INDIRIZZO IP DEL SERVER
        TCP_PORT = 5005 #PORTA TCP CONNESSIONE AL SERVER
        BUFFER_SIZE = 1024 #DIMENSIONE BUFFER DI RICEZIONE RISPOSTA DAL SERVER
        sock = None #INIZIALIZZAZIONE SOCKET
    
    def connessione(self):
        #SE NON SONO ANCORA CONNESSO, ALLORA LANCIO LA CONNESSIONE
        global sock
        if sock == None :
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #CREO IL SOCKET
        	#print sock
        	sock.settimeout(0.3) #TIMEOUT DI CONNESSIONE A 300msec.
        	try:
			sock.connect((TCP_IP,TCP_PORT)) #LANCIO LA CONNESSIONE
                except socket.timeout,e:
                	print 'TIMEOUT DI CONNESSIONE' #SE ENTRO I 300ms LA CONNESSIONE FALLISCE VADO IN TIMEOUT
                    	sock.close
                    	sock = None
                        #continue
                except socket.error,e:
                    	print 'ERRORE DI CONNESSIONE ', e
                    	sock.close
                    	sock = None
                        #continue
    def disconnessione(self):
        #SE SONO CONNESSO MI DISCONNETTO
        global sock
        if sock != None:
            try:
                sock.close
                sock = None
            except socket.error, e:
                print 'ERRORE DI DISCONNESSIONE', e
                sock.close
                sock = None
                #continue
    def invio_dati(self,dati):
        #FUNZIONE DI INVIO DEI DATI (dati deve essere di tipo STRING o BUFFER)
        global sock
        if sock == None :
            print 'NESSUNA CONNESSIONE AL SERVER, PROVO A CONNETTERMI'
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #CREO IL SOCKET
        	#print sock
            sock.settimeout(0.3) #TIMEOUT DI CONNESSIONE A 300msec.
            try:
                sock.connect((TCP_IP,TCP_PORT)) #LANCIO LA CONNESSIONE
            except socket.timeout,e:
                print 'TIMEOUT DI CONNESSIONE' #SE ENTRO I 300ms LA CONNESSIONE FALLISCE VADO IN TIMEOUT
                sock.close
                sock = None
                #continue
            except socket.error,e:
                print 'ERRORE DI CONNESSIONE ', e
                sock.close
                sock = None
        else:
            try:
                sock.send(dati)
            except socket.error, e:
                print 'ERRORE NEL INVIO DEI DATI', e
                sock.close
                sock = None
                #continue
    def ricezione_dati(self):
        #FUNZIONE DI RICEZIONE DATI
        #IMPOSTO IL TIMEOUT DI CONNESSIONE A 200 ms
        if sock != None:
            sock.settimeout(0.2)
            try:
                dati_ricevuti = sock.recv(BUFFER_SIZE)
                return dati_ricevuti
            except socket.timeout, e:
                err = e.args[0]
                if err == 'timed out':
                    print 'NESSUNA RISPOSTA RICEVUTA'
                    #continue
                else:
                    print e
                    sys.exit(1)
        
                
    
                    
