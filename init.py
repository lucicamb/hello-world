# File: init.py - ok
# Date: 31 gen 23
# Note: programma di inizializzazione di DyGeo

''' facendo l'import da qui, le funzioni non si vedono
#---- import di librerie di funzioni utente ----
import sys
sys.path.append('..\python')
from costruzioni import *
'''

#---- settaggio per video 1920x1280 ----
#setviewport(-8,0,1600,967)
#setwindow(50)

#---- settaggio per prove ----
setviewport(451,100,1450,800)
setwindow(50)

#grid(True)  #attivazione delle linee del grid - QUI NON HA EFFETTO (ok)
#color('#00AA00')
#color(red)  #ERRORE non segnalato che blocca tutto

setcolor('red')            # colore di disegno  
#color('#BB0022')        # colore di disegno  - E' CLONE DI setcolor
setwidth(THIN)             # spessore delle linee    
setstate(DRAGABLE)         # stato degli oggetti grafici    
setprgpath("..\\python\\") # percorso dei programmi da eseguire
#setprgpath("..\\python\\Formalizzare\\") # percorso dei programmi da eseguire
#setmodpath("..\\python\\") # percorso dei moduli da importare
setmodpath(".") # percorso dei moduli da importare
setmodpath("..\\python\\modules\\") # percorso dei moduli da importare
#setmodpath(".\\") # percorso dei moduli da importare
seteditor("C:\\Program Files\\Notepad++\\notepad++.exe") # percorso dell'editor ok

setcolor('green')   

#ciao()  #c'e' in costruzioni.py
#Point((2,3),color='red',state=DRAGABLE)  #prova
#Point(INPUT,msg='seleziona punto rosso...',color='red',state=DRAGABLE)  #prova
