class CSVFile():
    
    def __init__(self, name):
        self.name = name

    def get_data(self):
        my_file = open(self.name, 'r')
        element = []
        if my_file == []:
            return None
        for line in my_file:
            element1 = line.strip("\n").split(',')
            if element1[0] != 'Date':
                element.append(element1)
        return element

# appoggio = CSVFile('shampoo_sales.csv')
# print('{}'.format(appoggio.get_data()))