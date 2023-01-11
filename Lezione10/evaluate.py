import unittest

class Model():
    def fit(self, data):
        # Fit non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato') 
        
    def predict(self, data):
        # Predict non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')

    def evaluate(self, data, window):
        # Evaluate non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
    def media_incrementi(self, data): 
        
        # check su data
        if type(data) is not list:
            raise Exception('data is not a list')
            return None
        if len(data) < 1:
            raise Exception('Not enough data to predict')
            return None
        
        prev_value = None
        somma_incrementi = 0
        for i, item in enumerate(data):
            if prev_value == None: #se sono al primo elemento della lista
                pass
            else: #se sono in un elemento diverso da primo
                incremento = item - prev_value
                somma_incrementi = somma_incrementi + incremento 
            prev_value = item
        media = somma_incrementi/i
        
        return media

    def predict(self, data):
        predict = data[-1] + self.media_incrementi(data)
        return predict

    def evaluate(self, data, window):
        lunghezza = len(data)
        errore_medio = 0;
        count = 0; #conta le iterazioni fatte
        for i in range(lunghezza - (window + 1)):
            predizione = self.predict([data[i], data[i+1], data[i+2]])
            errore = data[i+3] - predizione
            count = count+1
            if errore < 0:
                errore_medio = errore_medio - errore
            else:
                errore_medio = errore_medio + errore
                
        return errore_medio/count
            
        

#fit  di increment model
class FitIncrementModel(IncrementModel):
    def fit(self, data):
        return self.media_incrementi(data) # ritorna la media degli incrementi della prima lista
        
    def predict(self, data1, data2):
        fitted = self.fit(data1) # chiedo la media delgi incrementi della prima lista e la salvo in fitted
        predicted = self.media_incrementi(data2) #chiedo la media delgi incrementi della seconda lista e la salvo in predicted
        return (data2[-1] + (fitted + predicted)/2) #faccio la media aritmetica delle due medie incrementi e la aggiungo alle vendite dell'ultimo mese

    
    def evaluate(self, data_fit, data, window):
        lunghezza = len(data)
        errore_medio = 0;
        count = 0; #conta le iterazioni fatte
        for i in range(lunghezza - 4):
            predizione = self.predict(data_fit ,[data[i], data[i+1], data[i+2]])
            errore = data[i+4] - predizione
            count = count+1
            if errore < 0:
                errore_medio = errore_medio - errore
            else:
                errore_medio = errore_medio + errore
                
        return errore_medio/count

        


class CSVFile():
    
    def __init__(self, name):
        self.name = name

    def float_get_data(self): #getdata che prende solo i valori del csv (non le date) già convertiti in float
        try:
            my_file = open(self.name, 'r')
            element = []
            if my_file == []:
                return None
            for line in my_file:
            
                element1 = line.strip("\n").split(',') #element1 è la riga
                # print('{}'.format(element1)) #stampa la riga
                if element1[0] != 'Date':
                    element.append(float(element1[1]))
            return element
        except Exception as e:
            print('ho avuto un Errore Generico del tipo {}'.format(e))



appoggio = CSVFile('shampoo_sales.csv')
data = appoggio.float_get_data()
data_fit = data[0:24]
data_evaluate = data[24:36]




# test all
increment_model = IncrementModel()
risultato_i = increment_model.evaluate(data_evaluate, 3)
print('errore medio senza fit: {}'.format(risultato_i))

increment_model_fit = FitIncrementModel()
risultato_f = increment_model_fit.evaluate(data_fit, data_evaluate, 3)
print('errore medio con fit: {}'.format(risultato_f))