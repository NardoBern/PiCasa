from sys import exit
class pulse:
    # FUNZIONE DI INIZIALIZZAZIONE
    def inizializzazione(self):
        self.stato = False
        self.statoOld = False
        self.locked = False
        self.durata = 0
    
    def aggiorna_pulse(self,lunghezza):
        if not self.stato:
            self.durata = lunghezza
            self.stato = True
        else:
            if self.durata <= 0:
                self.stato = False
            else:
                self.durata = self.durata - 1
        
        
