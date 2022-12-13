import unittest

class Model():
    def fit(self, data):
        # Fit non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato') 
        
    def predict(self, data):
        # Predict non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
    def media(self, data): 
        
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
        media =  + somma_incrementi/i
        
        return media

    def predict(self, data):
        predict = data[-1] + self.media(data)
        return predict

#fit  di increment model
class FitIncrementModel(IncrementModel):
    def fit(self, data):
        return self.media(data)
        
    def predict(self, data1, data2):
        fitted = self.fit(data1)
        predicted = self.media(data2)
        return (data2[-1] + (fitted + predicted)/2)