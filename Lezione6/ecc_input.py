class CSVFile():
    
    def __init__(self, name):
        self.name = name
        if type(self.name) is not str:
            raise Exception('Ho avuto un errore, il nome del file deve esser euna stringa') 

    def get_data(self, start = None, end = None):

        try:
            # apro il file
            my_file = open(self.name, 'r')
            if my_file == [] or my_file == None:
                return None
            # faccio i check che start e end siano abbiano senso, altrimenti alzo un eccezione
            numero_righe = len(my_file.readlines())
            if start == None or end == None:
                raise Exception('Start and end cannot be None')
            if start < 0 or end < 0:
                raise Exception('Start and end must be greater than zero')
            if start > numero_righe or end > numero_righe:
                raise Exception('Invalid start or end')
            if end < start:
                raise Exception('End must be greater then start')
            # fin qui tutto ok 
            
            # legge riga per riga il csv e salva ogni element1 in riga in una lista "element"
            my_file = open(self.name, 'r')
            element = []
            i = 0
            for line in my_file:
                element1 = line.strip("\n").split(',')
                if element1[0] != 'Date':
                    if i >= start and i <= end:
                        element.append(element1)
                i = i + 1
            return element
        
        except Exception as e:
            print('ho avuto un Errore Generico del tipo "{}"'.format(e))

class NumericalCSVFile(CSVFile):
    
    # NuericalCSVFile è una sotto classe di CSVFile, riprende quindi lgi stessi attributi __init__ della classe genitore
    
    # il metodo get_data viene sovrascritto e cambia rispetto alla get_data della classe genitore, definisco la nuova get_data:
    def get_data(self, *args, **kwargs):
        original_list = super().get_data(*args, **kwargs) #con questo comando chiamo la get_data originale e salvo il suo return in una variabile original list
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

# esempio di utilizzo
appoggio = CSVFile('shampoo_sales.csv')
print('{}'.format(appoggio.get_data(3, 15)))