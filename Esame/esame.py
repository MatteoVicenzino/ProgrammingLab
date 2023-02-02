class ExamException(Exception):
    pass

class CSVFile():
    pass

class CSVTimeSeriesFile(CSVFile):

    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        #controllo l'esistenza del file
        try:
            my_file = open(self.name, 'r')
        except Exception as e:
            raise ExamException('Errore apertura del file: {}'.format(e))
        #controllo se è leggibile
        try:
            my_file.readline()
            my_file.close() #per resettare conto righe
        except Exception as e:
            raise ExamException('Errore: file non leggibile o vuoto, {}'.format(e))

        my_file = open(self.name, 'r')
        lista_di_liste = [] #creo lista vuotra che accoglierà le liste annidate
        for line in my_file:
            lista_annidata = line.strip('\n').split(',')
            if lista_annidata[0] != 'epoch': #salto intestazione tabella
                try:
                    #Converto silenziosamente gli epoch float in int
                    #stringa->float->int, perché non posso convertire
                    #stringa '12.5' -> int, non rappresenta un int
                    lista_annidata[0] = int(float(lista_annidata[0]))
                    lista_annidata[1] = float(lista_annidata[1])
                except:
                    #se epoch o temperatura non contengono valori numerici
                    #la conversione a float non andrà a buon fine
                    #quindi ignoro quella riga
                    continue
                lista_di_liste.append(lista_annidata)

        #controllo per epoch fuori ordine o duplicato
        for i in range(len(lista_di_liste)-1): #scorro la lista fino al penultimo
            if lista_di_liste[i+1][0] <= lista_di_liste[i][0]:
                raise ExamException('Errore: lista non ordinata o timestamp duplicato')

        my_file.close()
        return lista_di_liste


def day_arrangement(time_series):

    lista_giornate = [] #creo lista di liste
    daily_values = [] #contiene tutte le temperature di una singola giornate
    for i in range(len(time_series)):
        if i == 0: #caso primo valore: lo aggiungo a daily_values
            daily_values = [time_series[i][1]]
        elif time_series[i][0] == time_series[i-1][0]: 
            #se il giorno è uguale al precedente
            #aggiungo il valore ad una stessa daily_values
            daily_values.append(time_series[i][1]) 
        else:
            #se invece è diverso 
            #sovrascrivo daily_values dopo averla aggiunta alla lista delle giornate
            lista_giornate.append(daily_values)
            daily_values = [time_series[i][1]]
        if i == len(time_series)-1: #caso ultimo valore: 
            #aggiungo l'ultima giornata alla lista delle giornate
            lista_giornate.append(daily_values)
            
    return lista_giornate


def compute_daily_max_difference(time_series):

    if type(time_series) is not list: #controllo su input
        raise ExamException('Errore: l\'argomento deve essere una lista')
    #converto gli epoch da secondi in giorni
    for item in time_series:
        coppia = item
        val_pre = coppia[0] #è il valore pre conversione
        #dividendo per il numero di secondi in un giorno:
        day_start_epoch = val_pre / 86400
        #converto ad int, per toglire la parte decimale che rappresenta i secondi
        coppia[0] = int(day_start_epoch)
    #time_series ora contiene epoch in giorni
    
    lista_giornate = day_arrangement(time_series) #temperature divise per giornata
    
    differenze = [] #lista delle differenze che ritornerò alla fine
    for i in range(len(lista_giornate)):
        if len(lista_giornate[i]) <= 1: 
            #Se non c'è almeno una misurazione per giorno, la differenza di quel giorno sarà None
            differenze.append(None)
        else:
            escursione_termica = max(lista_giornate[i]) - min(lista_giornate[i])
            differenze.append(escursione_termica)
    return differenze
