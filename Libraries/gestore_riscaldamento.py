##############################
#### CLASSE RISCALDAMENTO ####
#############################################################
#### MODALITA DI FUNZIONAMENTO MANUALE: 				 ####
#### SE NON HO L'AUTOMATICO ALLORA SEGUO IL COMANDO CHE  ####
#### LEGGO DAL DATABASE DATA_COMMANDS 					 ####
#############################################################
####################################################################
#### MODALITA DI FUNZIONAMENTO AUTOMATICO:                      ####
#### SE SONO IN AUTOMATICO ALLORA CONTROLLO SE PER QUELL ORA    ####
#### DEVE ESSERE ON OPPURE OFF (DAL DATABASE DATA_COMMANDS)     ####
####################################################################
import wiringpi2 as wiringpi
class riscaldamento:
    #####################################
    #### ROUTINE DI INIZIALIZZAZIONE ####
    #####################################
    def inizializzazione(self,indirizzo_uscita_comando,indirizzo_fdback_ev):
        self.stato = False
        self.statoOld = False
        self.indirizzo_uscita = indirizzo_uscita_comando
        wiringpi.digitalWrite(self.indirizzo_uscita,0)
        self.automatico = False
        self.contatore_manuale = 0
        self.dbUpdateCounter = 0
        self.countDownValue = 0
        self.stato_ev = False
        self.indirizzo_feedback_ev = indirizzo_fdback_ev
        self.comando_manuale = False
        self.comando_automatico = False
        self.set_contatore_manuale = 0
        self.databaseUpdateRequired = False
        self.backToAuto = False
        self.newEvent = False
        self.Event = ''
        self.ricettaAttuale = []

    ########################################################################
    #### ROUTINE DI GESTIONE DEL COMANDO VEDI COMMENTI IN TESTA AL FILE ####
    ########################################################################
    def gestionecomandoManuale(self):
        self.newEvent = False
        self.Event = ''
        if not self.automatico:
            if not self.stato and self.comando_manuale:
                wiringpi.digitalWrite(self.indirizzo_uscita,1)
                self.stato = True
                self.contatore_manuale = self.set_contatore_manuale * 60
                self.countDownValue = self.set_contatore_manuale
                print 'COUNTDOWN VALUE'
                print self.countDownValue
                self.dbUpdateCounter = 0
                self.backToAuto = False
                print 'ci sono passato'
                print self.contatore_manuale
                self.databaseUpdateRequired = True
                self.newEvent = True
                self.Event = 'ACCENSIONE MANUALE'
            if self.stato:
                self.contatore_manuale = self.contatore_manuale - 1
                self.dbUpdateCounter = self.dbUpdateCounter + 1
                print 'DECREMENTO CONTATORE!!'
                print self.contatore_manuale
                print 'DB UPDATE COUNTER'
                print self.dbUpdateCounter
                self.stato_ev = wiringpi.digitalRead(self.indirizzo_feedback_ev)
                if self.dbUpdateCounter > 59:
                    print 'AGGIORNO IL COUNTDOWN SUL DATABASE'
                    self.countDownValue = int(self.contatore_manuale/60)
                    print 'COUNTDOWN VALUE'
                    self.countDownValue
                    self.databaseUpdateRequired = True
                    self.dbUpdateCounter = 0
                if self.contatore_manuale <= 0 or not self.comando_manuale:
                    wiringpi.digitalWrite(self.indirizzo_uscita,0)
                    self.stato = False
                    self.contatore_manuale = 0
                    self.comando_manuale = False
                    self.backToAuto = True
                    self.databaseUpdateRequired = True
                    self.newEvent = True
                    self.Event = 'SPEGNIMENTO MANUALE'
    
    def gestioneComandoAutomatico(self,oraAttuale):
        self.newEvent = False
        self.Event = ''
        self.comando_automatico = self.ricettaAttuale[oraAttuale]
        if self.automatico and not self.stato and self.comando_automatico:
            self.stato = True
            wiringpi.digitalWrite(self.indirizzo_uscita,1)
            self.databaseUpdateRequired = True
            self.newEvent = True
            self.Event = 'ACCENSIONE AUTOMATICA'
        elif self.automatico and self.stato and not self.comando_automatico:
            self.stato = False
            wiringpi.digitalWrite(self.indirizzo_uscita,0)
            self.databaseUpdateRequired = True
            self.newEvent = True
            self.Event = 'SPEGNIMENTO AUTOMATICO'
        
