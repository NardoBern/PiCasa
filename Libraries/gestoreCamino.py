import wiringpi2 as wiringpi

class camino:
    def inizializzazione(self,indirizzoUscita):
        self.stato = 0
        self.comandoManuale = False
        self.comandoAutomatico = False
        self.automatico = False
        self.databaseUpdateRequired = True
        self.outputAddress = indirizzoUscita
        self.ricettaAttuale = []
        self.temperatureArray = []
        self.newEvent = False
        self.Event = ''
        self.iCurrentState = 0
        self.iCurrentStateTime = 0
        self.iCadenziatoreStateMachine = 0
        self.strCurrentState = ''
        
    def gestioneComandoManuale(self):
        print 'GESTIONE COMANDO MANUALE CAMINO'
        self.newEvent = False
        self.Event = ''
        if self.stato == 0 and not self.automatico and self.comandoManuale:
            self.stato = 1
            wiringpi.digitalWrite(self.outputAddress,1)
            self.databaseUpdateRequired = True
            self.newEvent = True
            self.Event = 'ACCENSIONE MANUALE'
            self.iCurrentState = 10
            self.strCurrentState = 'CAMINO IN ACCENSIONE'
            del self.temperatureArray[:]
        elif self.stato != 0 and not self.comandoManuale:
            self.stato = 0
            wiringpi.digitalWrite(self.outputAddress,0)
            self.databaseUpdateRequired = True
            self.newEvent = True
            self.Event = 'SPEGNIMENTO MANUALE'
            self.iCurrentState = 0
            self.strCurrentState = 'CAMINO COMANDATO A SPEGNERSI'
    
    def gestioneComandoAutomatico(self,oraAttuale):
        print 'GESTIONE COMANDO AUTOMATICO CAMINO'
        self.newEvent = False
        self.Event = ''
        self.comandoAutomatico = self.ricettaAttuale[oraAttuale]
        if self.stato == 0 and self.automatico and self.comandoAutomatico:
            self.stato = 1
            wiringpi.digitalWrite(self.outputAddress,1)
            self.databaseUpdateRequired = True
            self.newEvent = True
            self.Event = 'ACCENSIONE AUTOMATICA'
            self.iCurrentState = 10
            self.strCurrentState = 'CAMINO IN ACCENSIONE'
        elif self.automatico and self.stato != 0 and not self.comandoAutomatico:
            self.stato = 0
            wiringpi.digitalWrite(self.outputAddress,0)
            self.databaseUpdateRequired = True
            self.newEvent = True
            self.Event = 'SPEGNIMENTO AUTOMATICO'
            self.iCurrentState = 0
            self.strCurrentState = 'CAMINO COMANDATO A SPEGNERSI'
    
    def gestioneMacchinaStati(self,temp1,temp2,deltaTime):
        #### FUNZIONE DI GESTIONE MACCHINA A STATI DEL CAMINO -- DA RICHIAMARE OGNI 10 MINUTI ####
        print 'GESTIONE MACCHINA A STATI CAMINO'
        self.newEvent = False
        self.Event = ''

        if self.iCurrentState == 0:
            self.strCurrentState = 'CAMINO SPENTO'
            if self.stato == 1:
                self.iCurrentState = 10
                self.iCurrentStateTime = 0
                self.newEvent = True
                self.Event = 'CAMINO IN ACCENSIONE'

        if self.iCurrentState == 10:
            self.strCurrentState = 'CAMINO IN ACCENSIONE'
            print self.strCurrentState
            self.iCurrentStateTime = self.iCurrentStateTime + 1
            if self.stato != 0 and ((temp1-temp2)/deltaTime) > 0.5:
                self.iCurrentState = 20
                self.iCurrentStateTime = 0
                self.newEvent = True
                self.Event = 'CAMINO ACCESO'
            if self.stato != 0 and ((temp1-temp2)/deltaTime) < 0.2 and self.iCurrentStateTime >= 2:
                self.iCurrentState = 900
                self.iCurrentStateTime = 0
                self.newEvent = True
                self.Event = 'ACCENSIONE FALLITA'

        if self.iCurrentState == 20:
            self.strCurrentState = 'CAMINO ACCESO'
            print self.strCUrrentState
            self.iCurrentStateTime = self.iCurrentStateTime + 1
            if self.stato != 0 and ((temp1-temp2)/deltaTime) < 0:
                self.iCurrentState = 25
                self.iCurrentStateTime = 0
                self.newEvent = True
                self.Event = 'CAMINO ACCESO - PELLET IN ESAURIMENTO'

        if self.iCurrentState == 25:
            self.strCurrentState = 'CAMINO ACCESO - PELLET IN ESAURIMENTO'
            print self.strCurrentState
            self.iCurrentStateTime = self.iCurrentStateTime + 1
            if self.stato != 0 and ((temp1-temp2)/deltaTime) > 0.2:
                self.iCurrentState = 20
                self.iCurrentStateTIme = 0
                self.newEvent = True
                self.Event = 'CAMINO ACCESO'
            if self.stato != 0 and ((temp1-temp2)/deltaTime) < 0 and self.iCurrentStateTime > 12:
                self.iCurrentState = 901
                self.iCurrentStateTime = 0
                self.newEvent = True
                self.Event = 'PELLET ESAURITO'

        if self.iCurrentState == 900:
            self.strCurrentState = 'ACCENSIONE FALLITA'
            print self.strCUrrentState
            if self.stato == 0:
                self.iCurrentState = 0

        if self.iCurrentState == 901:
            self.strCurrentState = 'PELLET ESAURITO'
            print self.strCUrrentState
            if self.stato == 0:
                self.iCurrentState = 0

        if self.iCurrentState > 0:
            if self.stato == 0:
                self.iCurrentState = 0
                self.iCurrentStateTime = 0
                self.newEvent = True
                self.Event = 'CAMINO COMANDATO A SPEGNERSI'
        
