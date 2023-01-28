import random

class Automa():

    def __init__(self):
        self.biancheria
        self.calzini
        self.maglia
        self.pantaloni
        self.calzatura
      
    #funzioni che vestono l'automa: ritornano 1 se l'azione è andata a buon fine
    def biancheria(self):
        self.biancheria = True
        return 1
        
    def calzini(self):
        self.calzini = True
        return 1
        
    def maglia(self):
        self.maglia = True
        return 0
        
    def pantaloni(self):
        self.pantaloni = True
        return 1
        
    def calzatura(self):
        self.calzatura = True
        return 1


#funzione esegui: gli dici che capo mettere e veste quel capo
#ritornano ciò che ritorna il metodo chiamato
def esegui(automa, capo):
    
    if capo == "biancheria":
        print("mi metto la biancheria")
        return(automa.biancheria())

    if capo == "calzini":
        print("mi metto i calzini")
        return(automa.calzini())

    if capo == "maglia":
        print("mi metto la maglia")
        return(automa.maglia())

    if capo == "pantaloni":
        print("mi metto i pantaloni")
        return(automa.pantaloni())

    if capo == "calzatura":
        print("mi metto le calzature")
        return(automa.calzatura())
        
    

#esempio TEST all
lista_capi = ["biancheria", "calzini", "maglia", "pantaloni", "calzatura"]

#corpo dello script che, capo per capo chiama esegui
vestito = False
automa = Automa()
while vestito != True:
    capo = random.choice(lista_capi)

    # (G1) gestire in caso il capo selezionato va contro la sequenza della procedura
    #if(order_check(capo) != True):
    #so che l'ordine è giusto, sennò non faccio nemmeno quello che segue:


    
    try: #provo a vestire il capo selezionato
        done = esegui(automa, capo)
        if done == 0:
            raise Exception("l'automa non è riuscito a mettersi {}".format(capo))
    except Exception as e: #se esegui non va a buon fine
        print("Problema hardware: {}".format(e))
    #tolgo il capo dalla lista per non tornare a sceglierlo casualmente
    lista_capi.remove(capo)    
    

    #vestito diventa true quando:
    #non ci sono più capi da mettere, l'automa si è messo tutto
    if len(lista_capi)<1:
        vestito = True
        print("automa vestito correttamente")
    