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
        original_list = super().get_data()
        numerical_list = []
        for item in original_list:
            coppia = item
            for i,item in enumerate(coppia):
                numerical_raw = []
                if i==0:
                    numerical_raw.append(item)
                else:
                    try:
                        numerical_raw.append(float(item))
                    except Exception as e:
                        print('Errore: {}'.format(e))

                #for item in numerical_raw:
                    #print('{}'.format(type(item)))
                    #print('{}'.format(item))

            if len(numerical_raw) <= len(coppia):
                numerical_list.append(numerical_raw)

        #for item in numerical_list:
            #print('{}'.format(type(item)))
            #print('{}'.format(item))
        return numerical_list
        

appoggio = NumericalCSVFile('shampoo_sales.csv')
print('{}'.format(appoggio.get_data()))