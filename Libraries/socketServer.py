## SOCKET SERVER CLASS ##
import socket
import sys

class socketServer:
    def inizializzazione(self,host_port):
        ## FUNZIONE DI INIZIALIZZAZIONE DEL SERVER SOCKET ##
        self.connected = False
        self.created = False
        try:
            self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print 'SERVER CREATED'
            self.server.bind(host_port)
            print 'SERVER BINDED'
            self.created = True
            #self.server.setblocking(0)
        except socket.error as msg:
            print 'SERVER CREATION ERROR: ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit

    def start_ascolto(self):
        ## FUNZIONE DI START ATTESA RICEZIONE DATI ##
        try:
            self.server.listen(10)
            print 'SERVER IN ASCOLTO'
            while True:
                conn, addr = self.server.accept()
                print 'SERVER CONNESSO CON: ' + addr[0] + ':' + str(addr[1])
                data = conn.recv(1024)
                print 'DATI RICEVUTI: ' + data
        except socket.error as msg:
            print 'SERVER START ERROR: ' + str(msg[0]) + ' Message ' + msg[1]

    def chiusura_server(self):
        ## FUNZIONE DI CHIUSURA DEL SERVER ##
        self.server.close()
        print 'SERVER CHIUSO'