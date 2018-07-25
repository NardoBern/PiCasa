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
from threading import Timer
from db_manager import database_engine
from time import sleep
from gestore_orologio import orologio
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
#####################################################
#### FUNZIONE DI GESTIONE DEI COMANDI AUTOMATICI ####
#####################################################
def gestione_comandi_automatici():
    try:
        print 'GESTIONE COMANDI AUTOMATICI LUCI'
        #####################################################
        #### FUNZIONE DI GESTIONE DEI COMANDI AUTOMATICI ####
        #####################################################
        ##################################################
        #### GESTIONE COMANDO AUTOMATICO LUCE VERANDA ####
        ##################################################
        luce_veranda.gestione_comando_automatico(scheda2.stato_ingressi[5],luce_veranda.set_contatore_automatico,scheda1.stato_ingressi[0])
        #################################################
        #### GESTIONE COMANDO AUTOMATICO LUCE CUCINA ####
        #################################################
        luce_cucina.gestione_comando_automatico(scheda2.stato_ingressi[4],luce_cucina.set_contatore_automatico,scheda1.stato_ingressi[1])
        ####################################################
        #### GESTIONE COMANDO AUTOMATICO LUCE ANTIBAGNO ####
        ####################################################
        luce_antibagno.gestione_comando_automatico(scheda2.stato_ingressi[1],luce_antibagno.set_contatore_automatico,scheda1.stato_ingressi[2])
        ########################################################
        #### GESTIONE COMANDO AUTOMATICO LUCE SALA LIBRERIA ####
        ########################################################
        luce_sala_libreria.gestione_comando_automatico(scheda3.stato_ingressi[0],luce_sala_libreria.set_contatore_automatico,scheda1.stato_ingressi[3])
        #######################################################
        #### GESTIONE COMANDO AUTOMATICO LUCE CAMERA LETTO ####
        #######################################################
        luce_camera_letto.gestione_comando_automatico(scheda2.stato_ingressi[7],luce_camera_letto.set_contatore_automatico,scheda3.stato_ingressi[1])
        ####################################################
        #### GESTIONE COMANDO AUTOMATICO LUCE CORRIDOIO ####
        ####################################################
        luce_corridoio.gestione_comando_automatico(scheda2.stato_ingressi[2],luce_corridoio.set_contatore_automatico,scheda3.stato_ingressi[2])
        ###############################################
        #### GESTIONE COMANDO AUTOMATICO LUCE SALA ####
        ###############################################
        luce_sala.gestione_comando_automatico(scheda2.stato_ingressi[3],luce_sala.set_contatore_automatico,scheda3.stato_ingressi[3])
        ###################################################
        #### GESTIONE COMANDO AUTOMATICO LUCE INGRESSO ####
        ###################################################
        luce_ingresso.gestione_comando_automatico(scheda2.stato_ingressi[6],luce_ingresso.set_contatore_automatico,scheda3.stato_ingressi[4])
        ################################################
        #### GESTIONE COMANDO AUTOMATICO LUCE BAGNO ####
        ################################################
        luce_bagno.gestione_comando_automatico(scheda2.stato_ingressi[0],luce_bagno.set_contatore_automatico,scheda3.stato_ingressi[5])
    except Exception,e:
        print 'ERRORE NELLA GESTIONE COMANDI AUTOMATICI'
        print e
        errore = 'ERRONE NELLA GESTIONE COMANDI AUTOMATICI: ',e
        gestioneErrore(errore)

#################################################
#### FUNZIONE DI LETTURA COMANDI LUCI DA HMI ####
#################################################
def lettura_comandi_luci_hmi():
    try:
        ##############################
        #### LETTURA COMANDI LUCI ####
        ##############################
        nuovi_comandi = data_commands.lettura_dato_multiplo('comandi_luci','COMANDO')
        comandi = []
        for row in nuovi_comandi:
            comandi.append(row[0])
        luce_veranda.comando_hmi = comandi[0]
        luce_cucina.comando_hmi = comandi[1]
        luce_antibagno.comando_hmi = comandi[2]
        luce_sala_libreria.comando_hmi = comandi[3]
        luce_camera_letto.comando_hmi = comandi[4]
        luce_corridoio.comando_hmi = comandi[5]
        luce_sala.comando_hmi = comandi[6]
        luce_ingresso.comando_hmi = comandi[7]
        luce_bagno.comando_hmi = comandi[8]
        luce_fuori_davanti.comando_hmi = comandi[9]
        ###################################
        #### APPLICAZIONE COMANDI LUCI ####
        ###################################
        luce_veranda.gestione_comando_hmi()
        luce_cucina.gestione_comando_hmi()
        luce_antibagno.gestione_comando_hmi()
        luce_sala_libreria.gestione_comando_hmi()
        luce_camera_letto.gestione_comando_hmi()
        luce_corridoio.gestione_comando_hmi()
        ##print "LUCE SALA COMANDO HMI"
        ##print luce_sala.comando_hmi
        ##print "LUCE SALA COMANDO HMI OLD"
        ##print luce_sala.comando_hmi_old
        luce_sala.gestione_comando_hmi()
        luce_ingresso.gestione_comando_hmi()
        luce_bagno.gestione_comando_hmi()
        luce_fuori_davanti.gestione_comando_hmi()
    except Exception,e:
        #print 'ERRORE NELLA LETTURA COMANDI LUCI'
        #print e
        errore = 'ERRORE NELLA LETTURA COMANDI LUCI: ', e
        gestioneErrore(errore)
########################################################
#### FUNZIONE DI GESTIONE CONTATORI AUTOMATICI LUCI ####
########################################################
def gestioneContatoriAutomaticiLuci():
    try:
        scheda2.lockInputUpdate = True
        scheda3.lockInputUpdate = True
        if len(scheda2.stato_ingressi) == 8 and len(scheda3.stato_ingressi) == 8:
            print 'START GESTIONE CONTATORI AUTOMATICI LUCI'
            luce_veranda.gestione_contatore_automatico(scheda2.stato_ingressi[5])
            luce_cucina.gestione_contatore_automatico(scheda2.stato_ingressi[4])
            luce_antibagno.gestione_contatore_automatico(scheda2.stato_ingressi[1])
            luce_sala_libreria.gestione_contatore_automatico(scheda3.stato_ingressi[0])
            luce_camera_letto.gestione_contatore_automatico(scheda2.stato_ingressi[7])
            luce_corridoio.gestione_contatore_automatico(scheda2.stato_ingressi[2])
            luce_sala.gestione_contatore_automatico(scheda2.stato_ingressi[3])
            luce_ingresso.gestione_contatore_automatico(scheda2.stato_ingressi[6])
            luce_bagno.gestione_contatore_automatico(scheda2.stato_ingressi[0])
            print 'FINE GESTIONE CONTATORI AUTOMATICI LUCI'
        else:
            print 'GESTIONE CONTATORI AUTOMATICI LUCI - ROUTINE SALTATA INDICI NON ESATTI'
        scheda2.lockInputUpdate = False
        scheda3.lockInputUpdate = False

    except Exception,e:
        print 'ERRORE NELLA GESTIONE CONTATORI AUTOMATICI LUCI'
        print e
        errore = 'ERRORE NELLA GESTIONE CONTATORI AUTOMATICI LUCI: ',e, len(scheda2.stato_ingressi), len(scheda3.stato_ingressi)
        gestioneErrore(errore)
def lettura_automatico_luci_hmi():
    try:
        #print "LETTURA COMANDI AUTOMATICI LUCI"
        ##############################
        #### LETTURA COMANDI LUCI ####
        ##############################
        nuovi_comandi = data_commands.lettura_dato_multiplo('comandi_luci','AUTOMATICO')
        comandi = []
        for row in nuovi_comandi:
            comandi.append(row[0])
        luce_veranda.automatico = comandi[0]
        luce_cucina.automatico = comandi[1]
        luce_antibagno.automatico = comandi[2]
        luce_sala_libreria.automatico = comandi[3]
        luce_camera_letto.automatico = comandi[4]
        luce_corridoio.automatico = comandi[5]
        luce_sala.automatico = comandi[6]
        luce_ingresso.automatico = comandi[7]
        luce_bagno.automatico = comandi[8]
        luce_fuori_davanti.automatico = comandi[9]
        if luce_veranda.automatico != luce_veranda.automaticoOld:
            luce_veranda.databaseUpdateRequired = True
        if luce_cucina.automatico != luce_cucina.automaticoOld:
            luce_cucina.databaseUpdateRequired = True
        if luce_antibagno.automatico != luce_antibagno.automaticoOld:
            luce_antibagno.databaseUpdateRequired = True
        if luce_bagno.automatico != luce_bagno.automaticoOld:
            luce_bagno.databaseUpdateRequired = True
        if luce_camera_letto.automatico != luce_camera_letto.automaticoOld:
            luce_camera_letto.databaseUpdateRequired = True
        #print "LUCE CORRIDOIO AUTOMATICO"
        #print luce_corridoio.automatico
        #print "LUCE CORRIDOIO AUTOMATICO OLD"
        ##print luce_corridoio.automaticoOld
        if luce_corridoio.automatico != luce_corridoio.automaticoOld:
            #print "ENTRO QUI DOVE NON DEVO ENTRARE"
            luce_corridoio.databaseUpdateRequired = True
        if luce_sala.automatico != luce_sala.automaticoOld:
            luce_sala.databaseUpdateRequired = True
        if luce_ingresso.automatico != luce_ingresso.automaticoOld:
            luce_ingresso.databaseUpdateRequired = True
        if luce_bagno.automatico != luce_bagno.automaticoOld:
            luce_bagno.databaseUpdateRequired = True
        if luce_fuori_davanti.automatico != luce_fuori_davanti.automaticoOld:
            luce_fuori_davanti.databaseUpdateRequired = True
        if luce_sala_libreria.automatico != luce_sala_libreria.automaticoOld:
            luce_sala_libreria.databaseUpdateRequired = True
        luce_veranda.automaticoOld = luce_veranda.automatico
        luce_cucina.automaticoOld = luce_cucina.automatico
        luce_antibagno.automaticoOld = luce_antibagno.automatico
        luce_sala_libreria.automaticoOld = luce_sala_libreria.automatico
        luce_camera_letto.automaticoOld = luce_camera_letto.automatico
        luce_corridoio.automaticoOld = luce_corridoio.automatico
        luce_sala.automaticoOld = luce_sala.automatico
        luce_ingresso.automaticoOld = luce_ingresso.automatico
        luce_bagno.automaticoOld = luce_bagno.automatico
        luce_fuori_davanti.automaticoOld = luce_fuori_davanti.automatico
        luce_sala_libreria.automaticoOld = luce_sala_libreria.automatico
    except Exception,e:
        #print 'ERRORE NELLA LETTURA AUTOMATICO LUCI'
        #print e
        errore = 'ERRORE NELLA LETTURA AUTOMATICO LUCI: ',e
        gestioneErrore(errore)
##########################################################
#### FUNZIONE DI AGGIORNAMENTO DEL DATABASE DATASTORE ####
##########################################################
def aggiornamentoDataStore():
    try:
        print 'ENTRO NELLA ROUTINE AGGIORNAMENTO DATASTORE'
        if luce_sala.databaseUpdateRequired:
            print 'LUCE SALA'
            print 'AGGIORNAMENTO DATASTORE @ LUCE SALA'
            data_store.scrittura_singola_db('punti_luce','STATO','luce_sala',luce_sala.stato_out)
            data_store.scrittura_singola_db('punti_luce','AUTOMATICO','luce_sala',luce_sala.automatico)
            data_store.scrittura_singola_db('punti_luce','CONTATORE_AUTO','luce_sala',luce_sala.auto_contatore)
            luce_sala.databaseUpdateRequired = False
        #print luce_corridoio.databaseUpdateRequired
        if luce_corridoio.databaseUpdateRequired:
            print 'LUCE CORRIDOIO'
            print 'AGGIORNAMENTO DATASTORE @ LUCE CORRIDOIO'
            data_store.scrittura_singola_db('punti_luce','STATO','luce_corridoio',luce_corridoio.stato_out)
            data_store.scrittura_singola_db('punti_luce','AUTOMATICO','luce_corridoio',luce_corridoio.automatico)
            data_store.scrittura_singola_db('punti_luce','CONTATORE_AUTO','luce_corridoio',luce_corridoio.auto_contatore)
            luce_corridoio.databaseUpdateRequired = False
        if luce_ingresso.databaseUpdateRequired:
            print 'LUCE INGRESSO'
            print 'AGGIORNAMENTO DATASTORE @ LUCE INGRESSO'
            data_store.scrittura_singola_db('punti_luce','STATO','luce_ingresso',luce_ingresso.stato_out)
            data_store.scrittura_singola_db('punti_luce','AUTOMATICO','luce_ingresso',luce_ingresso.automatico)
            data_store.scrittura_singola_db('punti_luce','CONTATORE_AUTO','luce_ingresso',luce_ingresso.auto_contatore)
            luce_ingresso.databaseUpdateRequired = False
        if luce_bagno.databaseUpdateRequired:
            print 'LUCE BAGNO'
            print 'AGGIORNAMENTO DATASTORE @ LUCE BAGNO'
            data_store.scrittura_singola_db('punti_luce','STATO','luce_bagno',luce_bagno.stato_out)
            data_store.scrittura_singola_db('punti_luce','AUTOMATICO','luce_bagno',luce_bagno.automatico)
            data_store.scrittura_singola_db('punti_luce','CONTATORE_AUTO','luce_bagno',luce_bagno.auto_contatore)
            luce_bagno.databaseUpdateRequired = False
        if luce_veranda.databaseUpdateRequired:
            print 'LUCE VERANDA'
            print 'AGGIORNAMENTO DATASTORE @ LUCE VERANDA'
            data_store.scrittura_singola_db('punti_luce','STATO','luce_veranda',luce_veranda.stato_out)
            data_store.scrittura_singola_db('punti_luce','AUTOMATICO','luce_veranda',luce_veranda.automatico)
            data_store.scrittura_singola_db('punti_luce','CONTATORE_AUTO','luce_veranda',luce_veranda.auto_contatore)
            luce_veranda.databaseUpdateRequired = False
        if luce_cucina.databaseUpdateRequired:
            print 'LUCE CUCINA'
            print 'AGGIORNAMENTO DATASTORE @ LUCE CUCINA'
            data_store.scrittura_singola_db('punti_luce','STATO','luce_cucina',luce_cucina.stato_out)
            data_store.scrittura_singola_db('punti_luce','AUTOMATICO','luce_cucina',luce_cucina.automatico)
            data_store.scrittura_singola_db('punti_luce','CONTATORE_AUTO','luce_cucina',luce_cucina.auto_contatore)
            luce_cucina.databaseUpdateRequired = False
        if luce_antibagno.databaseUpdateRequired:
            print 'LUCE ANTIBAGNO'
            print 'AGGIORNAMENTO DATASTORE @ LUCE ANTIBAGNO'
            data_store.scrittura_singola_db('punti_luce','STATO','luce_antibagno',luce_antibagno.stato_out)
            data_store.scrittura_singola_db('punti_luce','AUTOMATICO','luce_antibagno',luce_antibagno.automatico)
            data_store.scrittura_singola_db('punti_luce','CONTATORE_AUTO','luce_antibagno',luce_antibagno.auto_contatore)
            luce_antibagno.databaseUpdateRequired = False
        if luce_sala_libreria.databaseUpdateRequired:
            print 'LUCE SALA LIBRERIA'
            print 'AGGIORNAMENTO DATASTORE @ LUCE SALA LIBRERIA'
            data_store.scrittura_singola_db('punti_luce','STATO','luce_sala_libreria',luce_sala_libreria.stato_out)
            data_store.scrittura_singola_db('punti_luce','AUTOMATICO','luce_sala_libreria',luce_sala_libreria.automatico)
            data_store.scrittura_singola_db('punti_luce','CONTATORE_AUTO','luce_sala_libreria',luce_sala_libreria.auto_contatore)
            luce_sala_libreria.databaseUpdateRequired = False
        if luce_camera_letto.databaseUpdateRequired:
            print 'LUCE CAMERA LETTO'
            print 'AGGIORNAMENTO DATASTORE @ LUCE CAMERA LETTO'
            data_store.scrittura_singola_db('punti_luce','STATO','luce_camera_letto',luce_camera_letto.stato_out)
            data_store.scrittura_singola_db('punti_luce','AUTOMATICO','luce_camera_letto',luce_camera_letto.automatico)
            data_store.scrittura_singola_db('punti_luce','CONTATORE_AUTO','luce_camera_letto',luce_camera_letto.auto_contatore)
            luce_camera_letto.databaseUpdateRequired = False
        if luce_fuori_davanti.databaseUpdateRequired:
            print 'LUCE FUORI DAVANTI'
            print 'AGGIORNAMENTO DATASTORE @ LUCE FUORI DAVANTI'
            data_store.scrittura_singola_db('punti_luce','STATO','luce_fuori_davanti',luce_fuori_davanti.stato_out)
            data_store.scrittura_singola_db('punti_luce','AUTOMATICO','luce_fuori_davanti',luce_fuori_davanti.automatico)
            data_store.scrittura_singola_db('punti_luce','CONTATORE_AUTO','luce_fuori_davanti',luce_fuori_davanti.auto_contatore)
            luce_fuori_davanti.databaseUpdateRequired = False
        data_store.salva_dati()
    except Exception,e:
        print 'ERRORE NEL AGGIORNAMENTO DEL DATASTORE'
        print e
        errore = 'ERRORE NEL AGGIORNAMENTO DEL DATASTORE', e
        gestioneErrore(errore)
#################################
#### INTERRUPT AD UN SECONDO ####
#################################
def one_second_interrupt_function():
    try:
        ###############################################
        #### FUNZIONE DI INTERRUPT AD OGNI SECONDO ####
        ###############################################
        print 'INTERRUPT AD UN SECONDO AVVIATO'
        ###########################################
        #### AGGIORNAMENTO OROLOGIO DI SISTEMA ####
        ###########################################
        systemClock.letturaOrologio()
        #######################################
        #### TEST E LETTURA COMANDI DA HMI ####
        #######################################
        print 'CONTROLLO SE CI SONO NUOVI COMANDI DA HMI'
        readData = data_commands.lettura_dato_multiplo('update','NEED_UPDATE')
        update = []
        test_nuovo_comando = 0
        for row in readData:
            update.append(row[0])
        test_nuovo_comando = update[0]
        print 'TEST NUOVO COMANDO: ', test_nuovo_comando
        if test_nuovo_comando == 1:
            #### LEGGO I COMANDI DELLE LUCI ####
            lettura_comandi_luci_hmi()
            #### LEGGO LE IMPOSTAZIONI DI AUTOMATICO / MANUALE ####
            lettura_automatico_luci_hmi()
            data_commands.scrittura_singola_db('update','NEED_UPDATE','1',0)
            data_commands.salva_dati()
        ############################################
        #### GESTIONE CONTATORI AUTOMATICI LUCI ####
        ############################################
        gestioneContatoriAutomaticiLuci()
        ##########################################
        #### AGGIORNAMENTO DATI NEL DATASTORE ####
        ##########################################
        aggiornamentoDataStore()
        ########################################
        #### REIMPOSTAZIONE TIMER E RIAVVIO ####
        ########################################
        print 'REIMPOSTAZIONE TIMER'
        t = Timer(1.0,one_second_interrupt_function)
        t.start()
    except Exception,e:
        print 'ERRORE NELLA ONE SECOND INTERRUPT FUNCTION'
        print e
        errore = 'ERRORE NELLA ONE SECOND INTERRUPT FUNCTION: ', e
        gestioneErrore(errore)
#####################################
#### FUNZIONE DI GESTIONE ERRORE ####
#####################################
def gestioneErrore(messaggioErrore):
    systemClock.letturaOrologio()
    timeStamp = systemClock.lettura
    ErrorDatabase.inserisciRecord(messaggioErrore,timeStamp)
    ErrorDatabase.salva_dati()
    data_store.salva_dati()
    data_commands.salva_dati()
    python = sys.executable
    os.execl(python, python, * sys.argv)
def memorizzaEvento(evento):
    systemClock.letturaOrologio()
    timeStamp = systemClock.lettura
    EventDatabase.inserisciEvento(evento,timeStamp)
    EventDatabase.salva_dati()
###################################
#### CICLO DI INIZIALIZZAZIONE ####
###################################
#########################################################
#### INIZIALIZZAZIONE CONNESSIONE AL DATABASE ERRORI ####
#########################################################
print 'CONNESSIONE AL DATABASE DEGLI ERRORI'
ErrorDatabase = database_engine('/home/pi/db_imp_ele/error_store.db')
##############################################
#### INIZIALIZZAZIONE OROLOGIO DI SISTEMA ####
##############################################
try:
    print ("INIZIALIZZAZIONE OROLOGIO DI SISTEMA")
    systemClock = orologio()
    systemClock.inizializzazioneOrologio()
except:
    print "ERRORE NELLA INIZIALIZZAZIONE DELL'OROLOGIO"
time.sleep(0.5)
#########################################################
#### INIZIALIZZAZIONE CONNESSIONE AL DATABASE EVENTI ####
#########################################################
print 'CONNESSIONE AL DATABASE DEGLI ERRORI'
EventDatabase = database_engine('/home/pi/db_imp_ele/event_store.db')
memorizzaEvento('AVVIO DEL SISTEMA')
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
##############################################
#### INIZIALIZZAZIONE DATABASE DATA_STORE ####
##############################################
try:
    print 'INIZIALIZZAZIONE CONNESSIONE AL DATABASE DATA_STORE'
    data_store = database_engine('/home/pi/db_imp_ele/data_store.db')
    ##################################################
    #### INIZIALIZZAZIONE DATI TABELLA PUNTI LUCE ####
    ##################################################
    print 'INIZIALIZZAZIONE DATI TABELLA PUNTI LUCE'
    data_store.scrittura_singola_db('punti_luce','STATO','luce_veranda',luce_veranda.stato_out)
    data_store.scrittura_singola_db('punti_luce','STATO','luce_cucina',luce_cucina.stato_out)
    data_store.scrittura_singola_db('punti_luce','STATO','luce_antibagno',luce_antibagno.stato_out)
    data_store.scrittura_singola_db('punti_luce','STATO','luce_sala_libreria',luce_sala_libreria.stato_out)
    data_store.scrittura_singola_db('punti_luce','STATO','luce_camera_letto',luce_camera_letto.stato_out)
    data_store.scrittura_singola_db('punti_luce','STATO','luce_corridoio',luce_corridoio.stato_out)
    data_store.scrittura_singola_db('punti_luce','STATO','luce_sala',luce_sala.stato_out)
    data_store.scrittura_singola_db('punti_luce','STATO','luce_ingresso',luce_ingresso.stato_out)
    data_store.scrittura_singola_db('punti_luce','STATO','luce_bagno',luce_bagno.stato_out)
    data_store.scrittura_singola_db('punti_luce','STATO','luce_fuori_davanti',luce_fuori_davanti.stato_out)
    data_store.scrittura_singola_db('punti_luce','AUTOMATICO','luce_veranda',luce_veranda.automatico)
    data_store.scrittura_singola_db('punti_luce','AUTOMATICO','luce_cucina',luce_cucina.automatico)
    data_store.scrittura_singola_db('punti_luce','AUTOMATICO','luce_antibagno',luce_antibagno.automatico)
    data_store.scrittura_singola_db('punti_luce','AUTOMATICO','luce_sala_libreria',luce_sala_libreria.automatico)
    data_store.scrittura_singola_db('punti_luce','AUTOMATICO','luce_camera_letto',luce_camera_letto.automatico)
    data_store.scrittura_singola_db('punti_luce','AUTOMATICO','luce_corridoio',luce_corridoio.automatico)
    data_store.scrittura_singola_db('punti_luce','AUTOMATICO','luce_sala',luce_sala.automatico)
    data_store.scrittura_singola_db('punti_luce','AUTOMATICO','luce_ingresso',luce_ingresso.automatico)
    data_store.scrittura_singola_db('punti_luce','AUTOMATICO','luce_bagno',luce_bagno.automatico)
    data_store.scrittura_singola_db('punti_luce','AUTOMATICO','luce_fuori_davanti',luce_fuori_davanti.automatico)
    data_store.scrittura_singola_db('punti_luce','CONTATORE_AUTO','luce_veranda',luce_veranda.auto_contatore)
    data_store.scrittura_singola_db('punti_luce','CONTATORE_AUTO','luce_cucina',luce_cucina.auto_contatore)
    data_store.scrittura_singola_db('punti_luce','CONTATORE_AUTO','luce_antibagno',luce_antibagno.auto_contatore)
    data_store.scrittura_singola_db('punti_luce','CONTATORE_AUTO','luce_sala_libreria',luce_sala_libreria.auto_contatore)
    data_store.scrittura_singola_db('punti_luce','CONTATORE_AUTO','luce_camera_letto',luce_camera_letto.auto_contatore)
    data_store.scrittura_singola_db('punti_luce','CONTATORE_AUTO','luce_corridoio',luce_corridoio.auto_contatore)
    data_store.scrittura_singola_db('punti_luce','CONTATORE_AUTO','luce_sala',luce_sala.auto_contatore)
    data_store.scrittura_singola_db('punti_luce','CONTATORE_AUTO','luce_ingresso',luce_ingresso.auto_contatore)
    data_store.scrittura_singola_db('punti_luce','CONTATORE_AUTO','luce_bagno',luce_bagno.auto_contatore)
    data_store.scrittura_singola_db('punti_luce','CONTATORE_AUTO','luce_fuori_davanti',luce_fuori_davanti.auto_contatore)
    data_store.scrittura_singola_db('punti_luce','SET_CONTATORE_AUTO','luce_veranda',luce_veranda.set_contatore_automatico)
    data_store.scrittura_singola_db('punti_luce','SET_CONTATORE_AUTO','luce_cucina',luce_cucina.set_contatore_automatico)
    data_store.scrittura_singola_db('punti_luce','SET_CONTATORE_AUTO','luce_antibagno',luce_antibagno.set_contatore_automatico)
    data_store.scrittura_singola_db('punti_luce','SET_CONTATORE_AUTO','luce_sala_libreria',luce_sala_libreria.set_contatore_automatico)
    data_store.scrittura_singola_db('punti_luce','SET_CONTATORE_AUTO','luce_camera_letto',luce_camera_letto.set_contatore_automatico)
    data_store.scrittura_singola_db('punti_luce','SET_CONTATORE_AUTO','luce_corridoio',luce_corridoio.set_contatore_automatico)
    data_store.scrittura_singola_db('punti_luce','SET_CONTATORE_AUTO','luce_sala',luce_sala.set_contatore_automatico)
    data_store.scrittura_singola_db('punti_luce','SET_CONTATORE_AUTO','luce_ingresso',luce_ingresso.set_contatore_automatico)
    data_store.scrittura_singola_db('punti_luce','SET_CONTATORE_AUTO','luce_bagno',luce_bagno.set_contatore_automatico)
    data_store.scrittura_singola_db('punti_luce','SET_CONTATORE_AUTO','luce_fuori_davanti',luce_fuori_davanti.set_contatore_automatico)
    data_store.salva_dati()
except Exception,e:
    print 'ERRORE NELLA CONNESSIONE AL DATABASE DATA_STORE'
    print e
try:
    ################################################################
    #### INIZIALIZZAZIONE CONNESSIONE AL DATABASE DATA_COMMANDS ####
    ################################################################
    print 'INIZIALIZZAZIONE CONNESSIONE AL DATABASE DATA_COMMANDS'
    data_commands = database_engine('/home/pi/db_imp_ele/data_commands.db')
except Exception,e:
    print 'ERRORE NELLA INIZIALIZZAZIONE DELLA CONNESSIONE AL DATABASE DATA_COMMANDS'
    print e
####################################################
#### INIZIALIZZAZIONE TIMER INTERRUPT AD 1 SEC. ####
####################################################
try:
    print 'INIZIALIZZAZIONE ONE SECOND INTERRUPT'
    t = Timer(1.0,one_second_interrupt_function)
    t.start()
except:
    print 'ERRORE NELLA INIZIALIZZAZIONE DEL TIMER DI INTERRUPT'
    t.cancel()
print 'FINE CICLO DI INIZIALIZZAZIONE'
###############################
#### FINE INIZIALIZZAZIONE ####
###############################
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
