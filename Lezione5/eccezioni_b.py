class CSVFile():
    
    # classe CSVFILE ha un attributo “name“
    
    def __init__(self, name):
        self.name = name

    # get_data è un metodo della classe CSV file che:
    def get_data(self):
        try:
            
            #prova ad aprire il file
            my_file = open(self.name, 'r')
            element = []
            if my_file == []:
                return None
            
            # legge riga per riga il csv e salva ogni element1 in riga in una lista "element"
            for line in my_file:
                element1 = line.strip("\n").split(',')
                if element1[0] != 'Date':
                    element.append(element1)
            return element
        except Exception as e:
            
            # se none riesce alza un eccezione
            print('ho avuto un Errore Generico del tipo {}'.format(e))

class NumericalCSVFile(CSVFile):
    
    # NuericalCSVFile è una sotto classe di CSVFile, riprende quindi lgi stessi attributi __init__ della classe genitore
    
    # il metodo get_data viene sovrascritto e cambia rispetto alla get_data della classe genitore, definisco la nuova get_data:
    def get_data(self):
        original_list = super().get_data() #con questo comando chiamo la get_data originale e salvo il suo return in una variabile original list
        numerical_list = [] #creo una lista vuota che accoglierà le liste, ovvero le coppie

        for item in original_list: #per ogni elemento della get_data originale
            coppia = item # salvo ogni riga in una 
            numerical_raw = [] #creo una lista vuota che accoglierà i valori convertiti in float
            for i,item in enumerate(coppia): #per ognuno dei due elementi della coppia
                if i==0:
                    numerical_raw.append(item)
                else: #converto solamente il secondo
                    try:
                        numerical_raw.append(float(item))
                    except Exception as e:
                        print('Errore: {}'.format(e)) # se none riesce alza un eccezione

            # infine aggiungo ogni listina (coppia) all'interno della lista grande
            numerical_list.append(numerical_raw)

        return numerical_list
        

#esempio di utilizzo
#appoggio = NumericalCSVFile('shampoo_sales.csv')
#print('{}'.format(appoggio.get_data()))