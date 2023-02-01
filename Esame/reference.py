class ExamException(Exception):
    pass

#classe CSVFile vista a lezione
class CSVFile():
    def __init__(self, name):
        self.name = name #istanza con il nome del file da aprire

    def get_data(self):
        pass

class CSVTimeSeriesFile(CSVFile):
    def get_data(self):
        my_file = open(self.name)
        lista_di_liste = [] #creo una lista vuota che accoglierà le liste annidate
        
        #CONTROLLI PER IL FILE SE è VUOTO, INESISTENTE O NON LEGGIBILE

        for line in my_file:
            lista_annidata = line.strip('\n').split(',')
            if lista_annidata[0] != 'epoch': #aggiungo a lista_di_liste solamente le righe diverse dall'intestazione della tabella, che riconosco perché inizia con 'epoch'

                
                #prima di aggiungere ogni lista annidata, converto silenziosamente i timestamp in interi ma se i timestamp sono di tipi non convertibili alzo un eccezzione

                #analogamente le temperature, ma se il valore è vuoto, non numerico o non leggibile alzo un eccezione
                
                
                try: # provo a convertire i valori
                    lista_annidata[0] = int(float(lista_annidata[0]))
                    # stringa -> float -> int perché in python non posso convertire da stringa -> int se il valore rappresentato dalla stringa non è un intero
                    lista_annidata[1] = float(lista_annidata[1])
                except Exception as e:
                    lista_di_liste.append([None,None])
                    continue
                    #print('Errore: {}'.format(e)) #in modo che poi alzo l'errore solamente il valore rappresentato dalla stringa non è né int né float


                
                lista_di_liste.append(lista_annidata)

        return lista_di_liste




#funzione che dato il tempo eproch in formato INT, ritorna il tempo UTC in formato LISTA???
def eproch_to_UTC():
    pass

        
#funzione che calcola la differenza massima di tutte le giornate, e le ritorna in una lista
def compute_daily_max_difference(time_series):
    
    differenze = [] #creo una lista vuota che accoglierà le differenze di ogni giornata

    val_giornata = [[8, 9, 10], [33, 34, 35], [90, 100, 101]] # è la lista di valori temperatura di un particolare giorno

    
    #OTTENGO VALGIORNATA IN QUALCHE MODO
    
    
    # controlli sui valori di ogni giorno: almeno un elemento
    for i in range(len(val_giornata)): # per ogni lista contenuta in val_giornata
        if len(val_giornata[i]) < 1: # controlli sui valori di ogni giorno: almeno un elemento
            differenze.append(None)
        else: #calcolo la differenza se è tutto a posto
            escursione_termica = max(val_giornata[i]) - min(val_giornata[i])
            differenze.append(escursione_termica)

    return differenze
        


time_series_file = CSVTimeSeriesFile(name='vuoto.csv')
time_series = time_series_file.get_data()


for item in time_series:
    print(item)

print('\n')

differenze = compute_daily_max_difference(time_series)
print(differenze)






