import wiringpi2 as wiringpi
class antifurto:
    def inizializzazione(self,timeoutSirenaSet):
        self.stato = False
        self.databaseUpdateRequired = True
        self.setTimeoutSirena = timeoutSirenaSet
        self.timeout = self.setTimeoutSirena
        self.comandoSirena = False
        self.abilitazione = False
        self.scattato = False
    
    def gestioneSirena(self,indirizzoUscita):
        if self.scattato:
            self.timeout = self.timeout-1
            if self.timeout > 0 and not self.comandoSirena:
                self.comandoSirena = True
                wiringpi.digitalWrite(indirizzoUscita,1)
                self.databaseUpdateRequired = True
            elif self.timeout <= 0 and self.comandoSirena:
                self.comandoSirena = False
                wiringpi.digitalWrite(indirizzoUscita,0)
                self.databaseUpdateRequired = True
        else:
            self.comandoSirena = False
            wiringpi.digitalWrite(indirizzoUscita,0)
            self.timeout = self.setTimeoutSirena
    
    def gestioneAntifurto(self):
        if self.abilitazione and self.stato and not self.scattato:
            self.scattato = True
            self.databaseUpdateRequired = True
        elif not self.abilitazione and self.scattato:
            self.scattato = False
            self.databaseUpdateRequired = True