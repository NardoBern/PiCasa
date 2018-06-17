import wiringpi2 as wiringpi
class punto_luce:
	#####################################################
	#### Funzione di inizializzazione del punto luce ####
	#####################################################
    def inizializzazione(self,input_address,output_address):
        in_address = input_address
        self.out_address = output_address
        self.stato_out = False
        self.automatico = False
        self.automaticoOld = 0
        self.auto_contatore = 0
        self.set_contatore_automatico = 60
        wiringpi.digitalWrite(self.out_address,0)
        self.stato_in = True
        self.stato_in_old = True
        self.comando_hmi = 0
        self.comando_hmi_old = 0
        self.databaseUpdateRequired = False
    ########################################################################################
    #### Funzione di gestione manuale e prevista la seguente modalita di funzionamento: ####
    #### STATO	MODALITA	INGRESSO	COMANDO		CONTATORE							####
    #### OFF	MANUALE		ON			ON			OFF									####
    #### ON		MANUALE		ON			OFF			OFF									####
    ########################################################################################
    def gestione_comando_manuale(self):
        #self.databaseUpdateRequired = False
        if not self.automatico:
            if not self.stato_out:
                wiringpi.digitalWrite(self.out_address,1)
                self.stato_out = True
                self.databaseUpdateRequired = True
            else:
                wiringpi.digitalWrite(self.out_address,0)
                self.stato_out = False
                self.databaseUpdateRequired = True
        #return update

	###########################################################################################
	#### Funzione di gestione automatica e prevista la seguente modalita di funzionamento: ####
	#### STATO	MODALITA	INGRESSOAUTO	INGRESSOMAN	COMANDO		CONTATORE			   ####
	#### OFF	AUTO		ON				NA			ON			ON					   ####
	#### ON		AUTO		ON				NA			ON			INIZIALIZZATO		   ####
	#### ON		AUTO		OFF				NA			OFF			ZERO				   ####
	#### ON		AUTO		ON				ON			OFF			ZERO FORCED			   ####
    ###########################################################################################
    def gestione_comando_automatico(self,ingressoauto,setcontauto,ingressoman):
        self.auto_sens = ingressoauto
        #self.databaseUpdateRequired = False
        if self.automatico:
            ###################
            #### STATO OFF ####
            ###################
            if not self.stato_out:
                if self.auto_sens:
                    wiringpi.digitalWrite(self.out_address,1)
                    self.stato_out = True
                    self.auto_contatore = setcontauto
                    self.databaseUpdateRequired = True
            ##################
            #### STATO ON ####
            ##################
            else:
                if self.auto_sens:
                    self.auto_contatore = setcontauto
                if not self.auto_sens and self.auto_contatore <= 0:
                    wiringpi.digitalWrite(self.out_address,0)
                    self.stato_out = False
                    self.databaseUpdateRequired = True
                if not ingressoman:
                    wiringpi.digitalWrite(self.out_address,0)
                    self.stato_out = False
                    self.auto_contatore = 0
                    self.automatico = False
                    self.databaseUpdateRequired = True
        #return update
	#######################################################
	#### Funzione di gestione del contatore automatico ####
	#######################################################
    def gestione_contatore_automatico(self,ingressoauto):
        #self.databaseUpdateRequired = False
        if self.automatico:
            self.auto_sens = ingressoauto
            if not self.auto_sens and self.stato_out:
                self.auto_contatore = self.auto_contatore - 1
                self.databaseUpdateRequired = True
    #################################################
    #### FUNZIONE DI GESTIONE DEL COMANDO DA HMI ####
    #################################################
    def gestione_comando_hmi(self):
        #self.databaseUpdateRequired = False
        if self.comando_hmi != self.comando_hmi_old:
	        if not self.automatico:
	            if self.comando_hmi:
	                wiringpi.digitalWrite(self.out_address,1)
	                self.stato_out = True
	                self.databaseUpdateRequired = True
	            else:
	                wiringpi.digitalWrite(self.out_address,0)
	                self.stato_out = False
	                #print "GESTIONE COMANDO HMI -- SETTO A TRUE DATABASEUPDATEREQUIRED"
	                self.databaseUpdateRequired = True
        #return update
		self.comando_hmi_old = self.comando_hmi