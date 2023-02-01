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
        except Exception as e:
            raise ExamException('Errore: file non leggibile o vuoto')
            
        lista_di_liste = [] 
        for line in my_file:
            lista_annidata = line.strip('\n').split(',')
            if lista_annidata[0] != 'epoch': 
                try:
                    #Converto gli epoch float in interi silenziosamente
                    #stringa->float->int, perché non posso convertire
                    #stringa '12.5' direttamente in intero, non rappresenta un int
                    lista_annidata[0] = int(float(lista_annidata[0]))
                    lista_annidata[1] = float(lista_annidata[1])
                except Exception as e:
                    #se epoch o temperatura non contengono valori numerici
                    #la ocnversione a float non andrà a buon fine
                    #quindi ignoro quella riga
                    continue
                lista_di_liste.append(lista_annidata)

        #controllo per epoch fuori ordine o duplicato
        for i in range(len(lista_di_liste)-1): #scorro la lista fino al penultimo
            if lista_di_liste[i+1][0] <= lista_di_liste[i][0]:
                raise ExamException('Errore: lista non ordinata o timestampo duplicato')

        return lista_di_liste


def diff(time_series):
    
    #lista liste in cui ogni listina contiene i valori di una giornata
    lista_giornate = []
    daily_values = []
    for i in range(len(time_series)):
        if i == 0:
            daily_values = [time_series[i][1]]
        elif time_series[i][0] == time_series[i-1][0]: # se il giorno è uguale al precedente
            daily_values.append(time_series[i][1])
        else:
            #se invece è diverso sovrascrivo listina
            lista_giornate.append(daily_values)
            daily_values = [time_series[i][1]]
        if i == len(time_series)-1:
            lista_giornate.append(daily_values)
    
    
    differenze = []
    for i in range(len(lista_giornate)):
        
        if len(lista_giornate[i]) < 1: 
            #Se non c'è almeno una misurazione, la differenza di quel giorno sarà None
            differenze.append(None)
        else:
            escursione_termica = max(lista_giornate[i]) - min(lista_giornate[i])
            differenze.append(escursione_termica)
    return differenze


def compute_daily_max_difference(time_series):
    
    
    for item in time_series:
        coppia = item
        val_pre = coppia[0]
        day_start_epoch = val_pre / 86400
        coppia[0] = int(day_start_epoch)
    #lista uguale a time_series ma con sec -> giorni
    risultato = diff(time_series)
    
    return risultato




time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()


differenze = compute_daily_max_difference(time_series)

for item in differenze:
    print(item)