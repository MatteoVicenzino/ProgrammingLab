class CSVFile():
    
    def __init__(self, name):
        self.name = name

    def get_data(self):
        try:
            my_file = open(self.name, 'r')
            element = []
            if my_file == []:
                return None
            for line in my_file:
                element1 = line.strip("\n").split(',')
                if element1[0] != 'Date':
                    element.append(element1)
            return element
        except Exception as e:
            print('ho avuto un Errore Generico del tipo {}'.format(e))

class NumericalCSVFile(CSVFile):
    def get_data(self):
        string_data = super().get_data()
        numerical_data = []
        for string_row in string_data:
            numerical_row = []
            for i,element in enumerate(string_row):
                if i == 0:
                    numerical_row.append(element)
                else:
                    try:
                        numerical_row.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break
            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)
        return numerical_data

        
appoggio = NumericalCSVFile('shampoo_sales.csv')
print('{}'.format(appoggio.get_data()))