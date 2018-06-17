import wiringpi2 as wiringpi
from __builtin__ import False
##################################
#### CLASSE SENSORE ANTIFURTO ####
##################################
class sensorePresenza:
    #####################################
    #### ROUTINE DI INIZIALIZZAZIONE ####
    #####################################
    def inizializzazione(self,indirizzo_ingresso):
        self.stato = False
        self.indirizzo = indirizzo_ingresso
        self.abilitazione = False
        self.scattato = False
        self.presenza = False
        self.filtro = 3
        self.databaseUpdateRequired = True
    ##############################################
    #### ROUTINE DI AGGIORNAMENTO DELLO STATO ####
    ##############################################
    def aggiornaStato(self):
        if self.abilitazione:
            self.stato = wiringpi.digitalRead(self.indirizzo)
        else:
            self.stato = False
    #################################################
    #### ROUTINE DI AGGIORNAMENTO DELLA PRESENZA ####
    #################################################
    def aggiornamentoPresenza(self):
        if self.stato:
            self.filtro = self.filtro - 1
            if self.filtro == 0:
                if not self.presenza:
                    self.databaseUpdateRequired = True
                self.presenza = self.stato
                self.filtro = 3
        else:
            if self.presenza:
                self.presenza = False
                self.databaseUpdateRequired = True
                self.filtro = 3
            else:
                self.filtro = 3
class sensoreFinestra:
    #####################################
    #### ROUTINE DI INIZIALIZZAZIONE ####
    #####################################
    def inizializzazione(self,indirizzo_ingresso):
        self.stato = False
        self.indirizzo = indirizzo_ingresso
        self.abilitazione = False
        self.scattato = False
        self.databaseUpdateRequired = True
        
    ##############################################
    #### ROUTINE DI AGGIORNAMENTO DELLO STATO ####
    ##############################################
    def aggiornaStato(self):
        statoPrecendente = self.stato
        if self.abilitazione:
            self.stato = wiringpi.digitalRead(self.indirizzo)
        else:
            self.stato = False
        if self.stato != statoPrecendente:
            self.databaseUpdateRequired = True
            
       