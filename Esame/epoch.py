class CSVTimeSeriesFile():

    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        my_file = open(self.name)
        lista_di_liste = [] 
        #CONTROLLI PER IL FILE SE è VUOTO, INESISTENTE O NON LEGGIBILE
        for line in my_file:
            lista_annidata = line.strip('\n').split(',')
            if lista_annidata[0] != 'epoch': 
                try:
                    lista_annidata[0] = int(float(lista_annidata[0]))
                    lista_annidata[1] = float(lista_annidata[1])
                except Exception as e:
                    lista_di_liste.append([None,None])
                    continue
                lista_di_liste.append(lista_annidata)

        return lista_di_liste




def diff(time_series):

    val_giornata = []
    listina = []
    primo_epoch = time_series[0][0]
    for i in range(len(time_series)):
        if i == 0:
            listina = [time_series[i][1]]
        elif time_series[i][0] == time_series[i-1][0]: # se il giorno è uguale al precedente
            listina.append(time_series[i][1])
        else:
            #se invece è diverso sovrascrivo listina
            val_giornata.append(listina)
            listina = [time_series[i][1]]
        if i == len(time_series)-1:
            val_giornata.append(listina)
            print('A')
    
    
    differenze = []
    for i in range(len(val_giornata)):
        if len(val_giornata[i]) < 1:
            differenze.append(None)
        else:
            escursione_termica = max(val_giornata[i]) - min(val_giornata[i])
            differenze.append(escursione_termica)
    return differenze

#obbiettivo: avere una lista liste in cui ogni listina contiene i valori di una giornata
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

"""
print('\n')
for item in time_series:
    print(item)
"""

differenze = compute_daily_max_difference(time_series)


for item in differenze:
    print(item)
