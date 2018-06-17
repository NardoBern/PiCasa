import wiringpi2 as wiringpi
class scheda:
    #FUNZIONE DI INIZIALIZZAZIONE SCHEDA
    def inizializzazione(self):
        wiringpi.wiringPiSetup()                    # initializes wiringpi2  librery
        wiringpi.mcp23017Setup(self.output_start_address,self.i2c_address)   # sets i2c  pin e indirizzo
        #IMPOSTAZIONE DELLE USCITE
        for i in range(0,7):
            wiringpi.pinMode(self.output_start_address+i,1)      # sets GPA0 as output
            wiringpi.digitalWrite(self.output_start_address+i,0) # sets GPA0 as 0 (0V, off)
        #IMPOSTAZIONE DEGLI INGRESSI
        for i in range(0,7):
            wiringpi.pinMode(self.input_start_address+i,0)         # sets GPB0 as input
            wiringpi.pullUpDnControl(self.input_start_address+i,0) # internal pull-up and pull-down deactivated
        self.stato_ingressi = []
        self.lockInputUpdate = False
        self.stato_uscite = []
        for i in range(0,8):
            self.stato_uscite.append(False)    
    #FUNZIONE DI LETTURA DEGLI INGRESSI
    def lettura_ingressi(self):
        if not self.lockInputUpdate:
            self.stato_ingressi = []
            for i in range(0,8):
                self.stato_ingressi.append(wiringpi.digitalRead(self.input_start_address+i))
    
    #FUNZIONE DI SCRITTURA INGRESSI OLD
    def aggiornamento_ingressi_old(self):
        if not self.lockInputUpdate:
            self.stato_ingressi_old = []
            self.stato_ingressi_old = self.stato_ingressi
    
    #FUNZIONE DI SCRITTURA DI UNA USCITA
    def scrivi_uscita(self,indirizzoUscita,stato):
        wiringpi.digitalWrite(indirizzoUscita,stato)
    
