class ExamException(Exception):
    pass

#classe CSVFile vista a lezione
class CSVFile():
    def __init__(self, name):
        self.name = name #istanza con il nome del file da aprire

class CSVTimeSeriesFile(CSVFile):
    def get_data(self):
        try:
            my_file = open(self.name)
        except:
            raise ExamException('Errore: file ')
        lista_di_liste = [] #creo una lista vuota che accoglierà le liste annidate
        
        #CONTROLLI PER IL FILE SE è VUOTO, INESISTENTE O NON LEGGIBILE

        for line in my_file:
            lista_annidata = line.strip('\n').split(',')
            if lista_annidata[0] != 'epoch': #aggiungo a lista_di_liste solamente le righe diverse dall'intestazione della tabella, che riconosco perché inizia con 'epoch'
                lista_di_liste.append(lista_annidata)
        return lista_di_liste


#funzione che dato il tempo eproch in formato INT, ritorna il tempo UTC in formato LISTA
def eproch_to_UTC():
    

        
#funzione che calcola la differenza massima di tutte le giornate, e le ritorna in una lista
def compute_daily_max_difference(time_series):
    differenze = [] #creo una lista vuota che accoglierà le differenze di ogni giornata
    for item in time_series:
        pass

    return differenze
        


time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
print(time_series)

compute_daily_max_difference(time_series)