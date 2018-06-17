import wiringpi2 as wiringpi
class diagnosticEngine:
    def inizializzazione(self,ledRedAddress,ledYellowAddress,ledGreenAddress):
        self.enable = False
        self.readInput = False
        self.writeOutput = False
        self.ledRedState = False
        self.ledYellowState = False
        self.ledGreenState = False
        self.ledRedAddress = ledRedAddress
        wiringpi.digitalWrite(self.ledRedAddress,0)
        self.ledGreenAddress = ledGreenAddress
        wiringpi.digitalWrite(self.ledGreenAddress,0)
        self.ledYellowAddress = ledYellowAddress
        wiringpi.digitalWrite(self.ledYellowAddress,0)
    
    def comandaLed(self,colore,stato):
        if colore == 'rosso':
            self.ledRedState = stato
            wiringpi.digitalWrite(self.ledRedAddress,self.ledRedState)
        elif colore == 'giallo':
            self.ledYellowState = stato
            wiringpi.digitalWrite(self.ledYellowAddress,self.ledYellowState)
        elif colore == 'verde':
            self.ledGreenState = stato
            wiringpi.digitalWrite(self.ledGreenAddress,self.ledGreenState)
    

        