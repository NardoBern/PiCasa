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
from drive_scheda import scheda
from punto_luce import punto_luce
from connessione_ethernet import ethernet_connection
from threading import Timer
from time import sleep
from socketServer import socketServer
counter = 0
##############################
#### DEFINIZIONE FUNZIONI ####
##############################
#################################################
#### FUNZIONE DI ASSOCIAZIONE DEGLI INGRESSI ####
#################################################
def associazione_input():
    luce_veranda.stato_in = scheda1.stato_ingressi[0]
    luce_cucina.stato_in = scheda1.stato_ingressi[1]
    luce_antibagno.stato_in = scheda1.stato_ingressi[2]
    luce_sala_libreria.stato_in = scheda1.stato_ingressi[3]
    luce_camera_letto.stato_in = scheda3.stato_ingressi[1]
    luce_corridoio.stato_in = scheda3.stato_ingressi[2]
    luce_sala.stato_in = scheda3.stato_ingressi[3]
    luce_ingresso.stato_in = scheda3.stato_ingressi[4]
    luce_bagno.stato_in = scheda3.stato_ingressi[5]
    luce_fuori_davanti.stato_in = scheda3.stato_ingressi[6]
def associazione_input_old():
    luce_veranda.stato_in_old = scheda1.stato_ingressi_old[0]
    luce_cucina.stato_in_old = scheda1.stato_ingressi_old[1]
    luce_antibagno.stato_in_old = scheda1.stato_ingressi_old[2]
    luce_sala_libreria.stato_in_old = scheda1.stato_ingressi_old[3]
    luce_camera_letto.stato_in_old = scheda3.stato_ingressi_old[1]
    luce_corridoio.stato_in_old = scheda3.stato_ingressi_old[2]
    luce_sala.stato_in_old = scheda3.stato_ingressi_old[3]
    luce_ingresso.stato_in_old = scheda3.stato_ingressi_old[4]
    luce_bagno.stato_in_old = scheda3.stato_ingressi_old[5]
    luce_fuori_davanti.stato_in_old = scheda3.stato_ingressi_old[6]
#########################################
#### FUNZIONE DI ASSOCIAZIONE OUTPUT ####
#########################################
def associazione_output():
    scheda1.stato_uscite[0] = luce_veranda.stato_out
    scheda1.stato_uscite[1] = luce_cucina.stato_out
    scheda1.stato_uscite[2] = luce_antibagno.stato_out
    scheda1.stato_uscite[3] = luce_sala_libreria.stato_out
    scheda1.stato_uscite[4] = False
    scheda1.stato_uscite[5] = False
    scheda1.stato_uscite[6] = False
    scheda1.stato_uscite[7] = False
    scheda2.stato_uscite[0] = False
    scheda2.stato_uscite[1] = False
    scheda2.stato_uscite[2] = False
    scheda2.stato_uscite[3] = False
    scheda2.stato_uscite[4] = False
    scheda2.stato_uscite[5] = False
    scheda2.stato_uscite[6] = False
    scheda2.stato_uscite[7] = False
    scheda3.stato_uscite[0] = False
    scheda3.stato_uscite[1] = luce_camera_letto.stato_out
    scheda3.stato_uscite[2] = luce_corridoio.stato_out
    scheda3.stato_uscite[3] = luce_sala.stato_out
    scheda3.stato_uscite[4] = luce_ingresso.stato_out
    scheda3.stato_uscite[5] = luce_bagno.stato_out
    scheda3.stato_uscite[6] = luce_fuori_davanti.stato_out
    scheda3.stato_uscite[7] = False
    scheda4.stato_uscite[0] = False
    scheda4.stato_uscite[1] = False
    scheda4.stato_uscite[2] = False
    scheda4.stato_uscite[3] = False
    scheda4.stato_uscite[4] = False
    scheda4.stato_uscite[5] = False
    scheda4.stato_uscite[6] = False
    scheda4.stato_uscite[7] = False
##################################################################
#### FUNZIONE DI GENERAZIONE AZIONI ISTANTANEE DEGLI INGRESSI ####
#### CHIAMATA DIRETTAMENTE NEL MAIN                           ####
##################################################################
def azioni_ingressi():
    try:
        ###############################
        #### GESTIONE COMANDI LUCI ####
        ###############################
        print 'ELABORAZIONE INGRESSI VELOCI'
        if not luce_sala.stato_in and luce_sala.stato_in_old:
            luce_sala.gestione_comando_manuale()
        if not luce_corridoio.stato_in and luce_corridoio.stato_in_old:
            luce_corridoio.gestione_comando_manuale()
        if not luce_ingresso.stato_in and luce_ingresso.stato_in_old:
            luce_ingresso.gestione_comando_manuale()
        if not luce_bagno.stato_in and luce_bagno.stato_in_old:
            luce_bagno.gestione_comando_manuale()
        if not luce_veranda.stato_in and luce_veranda.stato_in_old:
            luce_veranda.gestione_comando_manuale()
        if not luce_cucina.stato_in and luce_cucina.stato_in_old:
            luce_cucina.gestione_comando_manuale()
        if not luce_antibagno.stato_in and luce_antibagno.stato_in_old:
            luce_antibagno.gestione_comando_manuale()
        if not luce_sala_libreria.stato_in and luce_sala_libreria.stato_in_old:
            luce_sala_libreria.gestione_comando_manuale()
        if not luce_camera_letto.stato_in and luce_camera_letto.stato_in_old:
            luce_camera_letto.gestione_comando_manuale()
        if not luce_fuori_davanti.stato_in and luce_fuori_davanti.stato_in_old:
            luce_fuori_davanti.gestione_comando_manuale()
    except Exception,e:
        print 'ERRORE NELLA FUNZIONE AZIONI INGRESSI'
        errore = 'ERRORE NELLA FUNZIONE AZIONI INGRESSI: ', e
        gestioneErrore(errore)
        print e
def gestione_comandi_automatici():
    print 'GESTIONE COMANDI AUTOMATICI'
    ## TO BE DONE ##
#################################################
#### FUNZIONE DI LETTURA COMANDI LUCI DA HMI ####
#################################################
def lettura_comando_luci_hmi():
    try:
        print 'LETTURA COMANDO LUCI'
        ##############################
        #### LETTURA COMANDI LUCI ####
        ##############################

        ###################################
        #### APPLICAZIONE COMANDI LUCI ####
        ###################################

    except Exception,e:
        print 'ERRORE NELLA LETTURA COMANDI LUCI'
        print e
        errore = 'ERRORE NELLA LETTURA COMANDI LUCI: ', e
        gestioneErrore(errore)
def lettura_automatico_luci_hmi():
    try:
        print "LETTURA COMANDI AUTOMATICI LUCI"
        ##############################
        #### LETTURA COMANDI LUCI ####
        ##############################


        #if luce_veranda.automatico != luce_veranda.automaticoOld:
        #    luce_veranda.databaseUpdateRequired = True
        #if luce_cucina.automatico != luce_cucina.automaticoOld:
    #        luce_cucina.databaseUpdateRequired = True
    #    if luce_antibagno.automatico != luce_antibagno.automaticoOld:
    #        luce_antibagno.databaseUpdateRequired = True
    #    if luce_bagno.automatico != luce_bagno.automaticoOld:
    #        luce_bagno.databaseUpdateRequired = True
    #    if luce_camera_letto.automatico != luce_camera_letto.automaticoOld:
    #        luce_camera_letto.databaseUpdateRequired = True
        #print "LUCE CORRIDOIO AUTOMATICO"
        #print luce_corridoio.automatico
        #print "LUCE CORRIDOIO AUTOMATICO OLD"
        ##print luce_corridoio.automaticoOld
    #    if luce_corridoio.automatico != luce_corridoio.automaticoOld:
    #        #print "ENTRO QUI DOVE NON DEVO ENTRARE"
    #        luce_corridoio.databaseUpdateRequired = True
    #    if luce_sala.automatico != luce_sala.automaticoOld:
    #        luce_sala.databaseUpdateRequired = True
    #    if luce_ingresso.automatico != luce_ingresso.automaticoOld:
    #        luce_ingresso.databaseUpdateRequired = True
    #    if luce_bagno.automatico != luce_bagno.automaticoOld:
    #        luce_bagno.databaseUpdateRequired = True
    #    if luce_fuori_davanti.automatico != luce_fuori_davanti.automaticoOld:
    #        luce_fuori_davanti.databaseUpdateRequired = True
    #    if luce_sala_libreria.automatico != luce_sala_libreria.automaticoOld:
    #        luce_sala_libreria.databaseUpdateRequired = True
    #    luce_veranda.automaticoOld = luce_veranda.automatico
    #    luce_cucina.automaticoOld = luce_cucina.automatico
    #    luce_antibagno.automaticoOld = luce_antibagno.automatico
    #    luce_sala_libreria.automaticoOld = luce_sala_libreria.automatico
    #    luce_camera_letto.automaticoOld = luce_camera_letto.automatico
    #    luce_corridoio.automaticoOld = luce_corridoio.automatico
    #    luce_sala.automaticoOld = luce_sala.automatico
    #    luce_ingresso.automaticoOld = luce_ingresso.automatico
    #    luce_bagno.automaticoOld = luce_bagno.automatico
    #    luce_fuori_davanti.automaticoOld = luce_fuori_davanti.automatico
    #    luce_sala_libreria.automaticoOld = luce_sala_libreria.automatico
    except Exception,e:
        print 'ERRORE NELLA LETTURA AUTOMATICO LUCI'
        print e
        errore = 'ERRORE NELLA LETTURA AUTOMATICO LUCI: ',e
        gestioneErrore(errore)
def gestioneErrore(messaggioErrore):
    print 'GESTIONE ERRORE'
try:
    print 'INIZIALIZZAZIONE SCHEDA 1'
    scheda1 = scheda()
    scheda1.i2c_address = 0x21
    scheda1.output_start_address = 65
    scheda1.input_start_address = 73
    scheda1.inizializzazione()
except Exception,e:
    print 'ERRORE NELLA INIZIALIZZAZIONE DELLA SCHEDA 1'
    print e
    errore = 'ERRORE NELLA INIZIALIZZAZIONE DELLA SCHEDA 1: ', e
    gestioneErrore(errore)
    time.sleep(0.5)
###################################
#### INIZIALIZZAZIONE SCHEDA 2 ####
###################################
try:
    print 'INIZIALIZZAZIONE SCHEDA 2'
    scheda2 = scheda()
    scheda2.i2c_address = 0x22
    scheda2.output_start_address = 81
    scheda2.input_start_address = 89
    scheda2.inizializzazione()
except Exception,e:
    print 'ERRORE NELLA INIZIALIZZAZIONE DELLA SCHEDA 2'
    print e
    errore = 'ERRORE NELLA INIZIALIZZAZIONE DELLA SCHEDA 2: ', e
    gestioneErrore(errore)
time.sleep(0.5)
###################################
#### INIZIALIZZAZIONE SCHEDA 3 ####
###################################
try:
    print 'INIZIALIZZAZIONE SCHEDA 3'
    scheda3 = scheda()
    scheda3.i2c_address = 0x23
    scheda3.output_start_address = 97
    scheda3.input_start_address = 105
    scheda3.inizializzazione()
except Exception,e:
    print 'ERRORE NELLA INIZIALIZZAZIONE DELLA SCHEDA 3'
    print e
    errore = 'ERRORE NELLA INIZIALIZZAZIONE DELLA SCHEDA 3: ', e
    gestioneErrore(errore)
time.sleep(0.5)
###################################
#### INIZIALIZZAZIONE SCHEDA 4 ####
###################################
try:
    print 'INIZIALIZZAZIONE SCHEDA 4'
    scheda4 = scheda()
    scheda4.i2c_address = 0x24
    scheda4.output_start_address = 113
    scheda4.input_start_address = 121
    scheda4.inizializzazione()
except Exception,e:
    print 'ERRORE NELLA INIZIALIZZAZIONE DELLA SCHEDA 4'
    errore = 'ERRORE NELLA INIZIALIZZAZIONE DELLA SCHEDA 4:', e
    gestioneErrore(errore)
time.sleep(0.5)
#####################################
#### INIZIALIZZAZIONE PUNTI LUCE ####
#####################################
#############################################
#### INIZIALIZZAZIONE PUNTO LUCE VERANDA ####
#############################################
try:
	print 'INIZIALIZZAZIONE PUNTO LUCE VERANDA'
	luce_veranda = punto_luce()
	luce_veranda.inizializzazione(73,65)
except:
	print 'ERRORE INIZIALIZZAZIONE PUNTO LUCE VERANDA'
time.sleep(0.1)
############################################
#### INIZIALIZZAZIONE PUNTO LUCE CUCINA ####
############################################
try:
	print 'INIZIALIZZAZIONE PUNTO LUCE CUCINA'
	luce_cucina = punto_luce()
	luce_cucina.inizializzazione(74,66)
except:
	print 'ERRORE INIZIALIZZAZIONE PUNTO LUCE CUCINA'
time.sleep(0.1)
###############################################
#### INIZIALIZZAZIONE PUNTO LUCE ANTIBAGNO ####
###############################################
try:
	print 'INIZIALIZZAZIONE PUNTO LUCE ANTIBAGNO'
	luce_antibagno = punto_luce()
	luce_antibagno.inizializzazione(75,67)
except:
	print 'ERRORE INIZIALIZZAZIONE PUNTO LUCE ANTIBAGNO'
time.sleep(0.1)
###################################################
#### INIZIALIZZAZIONE PUNTO LUCE SALA LIBRERIA ####
###################################################
try:
	print 'INIZIALIZZAZIONE PUNTO LUCE SALA LIBRERIA'
	luce_sala_libreria = punto_luce()
	luce_sala_libreria.inizializzazione(76,68)
except:
	print 'ERRORE INIZIALIZZAZIONE PUNTO LUCE SALA LIBRERIA'
time.sleep(0.1)
##################################################
#### INIZIALIZZAZIONE PUNTO LUCE CAMERA LETTO ####
##################################################
try:
	print 'INIZIALIZZAZIONE PUNTO LUCE CAMERA LETTO'
	luce_camera_letto = punto_luce()
	luce_camera_letto.inizializzazione(106,98)
except:
	print 'ERRORE INIZIALIZZAZIONE PUNTO LUCE CAMERA LETTO'
time.sleep(0.1)
###############################################
#### INIZIALIZZAZIONE PUNTO LUCE CORRIDOIO ####
###############################################
try:
	print 'INIZIALIZZAZIONE PUNTO LUCE CORRIDOIO'
	luce_corridoio = punto_luce()
	luce_corridoio.inizializzazione(107,99)
except:
	print 'ERRORE INIZIALIZZAZIONE PUNTO LUCE CORRIDOIO'
time.sleep(0.1)
##########################################
#### INIZIALIZZAZIONE PUNTO LUCE SALA ####
##########################################
try:
	print 'INIZIALIZZAZIONE PUNTO LUCE SALA'
	luce_sala = punto_luce()
	luce_sala.inizializzazione(108,100)
except:
	print 'ERRORE INIZIALIZZAZIONE PUNTO LUCE SALA'
time.sleep(0.1)
##############################################
#### INIZIALIZZAZIONE PUNTO LUCE INGRESSO ####
##############################################
try:
	print 'INIZIALIZZAZIONE PUNTO LUCE INGRESSO'
	luce_ingresso = punto_luce()
	luce_ingresso.inizializzazione(109,101)
except:
	print 'ERRORE INIZIALIZZAZIONE PUNTO LUCE INGRESSO'
time.sleep(0.1)
###########################################
#### INIZIALIZZAZIONE PUNTO LUCE BAGNO ####
###########################################
try:
	print 'INIZIALIZZAZIONE PUNTO LUCE BAGNO'
	luce_bagno = punto_luce()
	luce_bagno.inizializzazione(110,102)
except:
	print 'ERRORE INIZIALIZZAZIONE PUNTO LUCE BAGNO'
time.sleep(0.1)
###################################################
#### INIZIALIZZAZIONE PUNTO LUCE FUORI DAVANTI ####
###################################################
try:
	print 'INIZIALIZZAZIONE PUNTO LUCE FUORI DAVANTI'
	luce_fuori_davanti = punto_luce()
	luce_fuori_davanti.inizializzazione(111,103)
except:
	print 'ERRORE INIZIALIZZAZIONE PUNTO LUCE FUORI DAVANTI'
time.sleep(0.1)
###################################
#### INIZIALIZZAZIONE INGRESSI ####
###################################
try:
    print 'INIZIALIZZAZIONE INGRESSI'
    scheda1.lettura_ingressi()
    scheda2.lettura_ingressi()
    scheda3.lettura_ingressi()
    scheda4.lettura_ingressi()
except:
    print 'ERRORE NELLA INIZIALIZZAZIONE INGRESSI'
time.sleep(0.5)
#######################################
#### INIZIALIZZAZIONE INGRESSI OLD ####
#######################################
try:
    print 'INIZIALIZAZZIONE INGRESSI OLD'
    scheda1.aggiornamento_ingressi_old()
    scheda2.aggiornamento_ingressi_old()
    scheda3.aggiornamento_ingressi_old()
    scheda4.aggiornamento_ingressi_old()
except:
    print 'ERRORE NELLA INIZIALIZZAZIONE DEGLI INGRESSI OLD'
########################################
#### INIZIALIZZAZIONE SERVER SOCKET ####
########################################
try:
    print 'INIZIALIZZAZIONE SERVER SOCKET'
    server = socketServer()
    server.inizializzazione('',1001)
    server.start_ascolto()
except:
    print 'ERRORE NELLA INIZIALIZZAZIONE DEL SERVER SOCKET'
#############################################
#### MAIN ROUTINE: ESEGUITA ALL'INFINITO ####
#############################################
while(True):
        ##########################
        #### LETTURA INGRESSI ####
        ##########################
        scheda1.lettura_ingressi()
        scheda2.lettura_ingressi()
        scheda3.lettura_ingressi()
        scheda4.lettura_ingressi()
        ###############################
        #### ASSOCIAZIONE INGRESSI ####
        ###############################
        associazione_input()
        #############################
        #### ASSOCIAZIONE USCITE ####
        #############################
        associazione_output()
        temp_messaggio = "INGRESSI SCHEDA 1:", scheda1.stato_ingressi
        print temp_messaggio
        temp_messaggio = "INGRESSI SCHEDA 2:", scheda2.stato_ingressi
        print temp_messaggio
        temp_messaggio = "INGRESSI SCHEDA 3:", scheda3.stato_ingressi
        print temp_messaggio
        temp_messaggio = "INGRESSI SCHEDA 4:", scheda4.stato_ingressi
        print temp_messaggio
        azioni_ingressi()
        gestione_comandi_automatici()
        ####################################
        #### AGGIORNAMENTO INGRESSI OLD ####
        ####################################
        scheda1.aggiornamento_ingressi_old()
        scheda2.aggiornamento_ingressi_old()
        scheda3.aggiornamento_ingressi_old()
        scheda4.aggiornamento_ingressi_old()
        associazione_input_old()
        counter = counter + 1
        if counter > 1000 :
            counter = 0
        print counter
        time.sleep(0.05)
