class CSVFile():
    
    def __init__(self, name):
        self.name = name
        if type(self.name) is not str:
            raise Exception('Ho avuto un errore, il nome del file deve esser euna stringa') 
            
    def get_data(self, start = None, end = None):
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

appoggio = CSVFile('shampoo_sales.csv')
print('{}'.format(appoggio.get_data(9, 24)))