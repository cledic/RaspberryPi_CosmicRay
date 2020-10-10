# RaspberryPi_CosmicRay

Ho usato una Raspberry 3 con la CMOS camera collegata. La camera era oscurata da una busta nera ricoperta di nastro isolante nero.

Per il software sono stato ispirato da un progetto free che ho trovato in Internet e che, oltre alla App Android, aveva un esempio per Raspberry. 

La mia versione una la RaspyCam perché ho raggiunto un buon frame-rate, da 20ms a 30ms max, ed ho usato tre programmi distinti per la gestione.

Il programma "CamLoopCV_ver0.02.py" è sempre in esecuzione in backbround ed acquisisce l'immagine utile dalla camera, solo se supera un determinato livello di soglia. Il file viene salvato in un folder sotto "tmp" che per me è una ramdisk che monto sotto "tmp" all'avvio dello script.

Il programma "CosmicImageSplit_ver0.02.py" estrae i singoli "DOT" trovati salvandoli separatamente e salvando in un file di testo "Report.lst" il nome dell'immagine da cui è stato estratto e le coordinate in cui appariva.

Il programma "CreateTotalEventImg_ver0.02.py" invece legge tutte le immagini salvate e le monta in una unica immagine con il nome di "totalEvent.png"

Nel folder "images" ci sono alcuni esempi di immagini che ho catturato.


