#!/usr/bin/python3
#!/usr/bin/env python

########################################
#### IMPORTAZIONE LIBRERIE / CLASSI ####
########################################
import time
import sys
import os
import datetime
import site
site.addsitedir(sys.path[0]+'/Libraries')
from socketClient import ethernet_connection

#### CREO UN NUOVO CLIENT ####
socketClient = ethernet_connection()

#### CONNESSIONE AL SERVER ####
socketClient.inizializzazione()
socketClient.connessione()
socketClient.invio_dati('81')
