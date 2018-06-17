from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
lcd = Adafruit_CharLCDPlate()
class lcd_display:
    #lcd = Adafruit_CharLCDPlate()
    ######################################
    #### INIZIALIZZAZIONE DISPLAY LCD ####
    ######################################
    def inizializzazione(self):
        self.btn = ((lcd.LEFT  , 'Pulsante 1' , lcd.BLUE),
                    (lcd.UP    , 'Pulsante 2' , lcd.BLUE),
                    (lcd.DOWN  , 'Pulsante 3' , lcd.BLUE),
                    (lcd.RIGHT , 'Pulsante 4' , lcd.BLUE),
                    (lcd.SELECT, ''           , lcd.ON))
        self.prev = -1
        self.enterButtonPressed = False
        self.leftButtonPressed = False
        self.rightButtonPressed = False
        self.upButtonPressed = False
        self.downButtonPressed = False
        self.enterButtonPressedOld = False
        self.leftButtonPressedOld = False
        self.rightButtonPressedOld = False
        self.upButtonPressedOld = False
        self.downButtonPressedOld = False
        self.ledState = False
        self.ledTimeOut = 30
        self.menuValue = 0
    ###############################
    #### PULIZIA DELLO SCHERMO ####
    ###############################
    def pulisciSchermo(self):
        lcd.clear()
    #####################################
    #### GESTIONE RETROILLUMINAZIONE ####
    #####################################
    def retroilluminazione(self,stato):
        if stato:
            lcd.backlight(lcd.ON)
            self.ledState = True
        else:
            lcd.backlight(lcd.OFF)
            self.ledState = False
            self.ledTimeOut = 30
    #########################
    #### SCRITTURA TESTO ####
    #########################
    def scrivi(self,messaggio):
        lcd.message(messaggio)
    #################################
    #### EVENTO PULSANTE PREMUTO ####
    #################################
    def leggiPulsanti(self):
        self.prev = -1
        self.leftButton = self.btn[0]
        self.upButton = self.btn[1]
        self.downButton = self.btn[2]
        self.rightButton = self.btn[3]
        self.enterButton = self.btn[4]
        if lcd.buttonPressed(self.enterButton[0]):
            self.enterButtonPressed = True
        else:
            self.enterButtonPressed = False
        if lcd.buttonPressed(self.leftButton[0]):
            self.leftButtonPressed = True
        else:
            self.leftButtonPressed = False
        if lcd.buttonPressed(self.rightButton[0]):
            self.rightButtonPressed = True
        else:
            self.rightButtonPressed = False
        if lcd.buttonPressed(self.upButton[0]):
            self.upButtonPressed = True
        else:
            self.upButtonPressed = False
        if lcd.buttonPressed(self.downButton[0]):
            self.downButtonPressed = True
        else:
            self.downButtonPressed = False
            
        if self.enterButtonPressed and not self.enterButtonPressedOld:
            if  not self.ledState:
                lcd.backlight(lcd.ON)
                self.ledState = True
            else:
                lcd.backlight(lcd.OFF)
                self.ledState = False
            
        if self.leftButtonPressed and not self.leftButtonPressedOld:
            lcd.scrollDisplayLeft()
            
        if self.rightButtonPressed and not self.rightButtonPressedOld:
            lcd.scrollDisplayRight()
            
        if self.upButtonPressed and not self.upButtonPressedOld:
            if self.menuValue != 4:
                self.menuValue = self.menuValue + 1
            else: 
                self.menuValue = 0
        
        if self.downButtonPressed and not self.downButtonPressedOld:
            if self.menuValue != 0:
                self.menuValue = self.menuValue - 1
            else: 
                self.menuValue = 4
        #if self.downButtonPressed and not self.downButtonPressedOld:
        #    print ("PULSANTE BASSO PREMUTO")
        self.downButtonPressedOld = self.downButtonPressed
        self.upButtonPressedOld = self.upButtonPressed
        self.enterButtonPressedOld = self.enterButtonPressed
        self.leftButtonPressedOld = self.leftButtonPressed
        self.rightButtonPressedOld = self.rightButtonPressed
##        self.downButtonPressed = False
##        self.enterButtonPressed = False
##        self.leftButtonPressed = False
##        self.rightButtonPressed = False
##        self.upButtonPressed = False
        