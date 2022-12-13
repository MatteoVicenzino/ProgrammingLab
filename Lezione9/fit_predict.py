import unittest

class Model():
    def fit(self, data):
        # Fit non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato') 
        
    def predict(self, data):
        # Predict non implementanto nella classe base
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
        media =  + somma_incrementi/i
        
        return media

    def predict(self, data):
        predict = data[-1] + self.media_incrementi(data)
        return predict

#fit  di increment model
class FitIncrementModel(IncrementModel):
    def fit(self, data):
        return self.media_incrementi(data) # ritorna la media degli incrementi della prima lista
        
    def predict(self, data1, data2):
        fitted = self.fit(data1) #chiedo la media delgi incrementi della prima lista e la salvo in fitted
        predicted = self.media_incrementi(data2) #chiedo la media delgi incrementi della seconda lista e la salvo in predicted
        return (data2[-1] + (fitted + predicted)/2) #faccio la media aritmetica delle due medie incrementi e la aggiungo alle vendite dell'ultimo mese
    

# unit test
"""
class TestIncrementModel(unittest.TestCase):
    
    def TestIncrementModel(self):
        try:
            increment_model = IncrementModel()
            self.assertEqual(increment_model.predict([]), None)
            self.assertEqual(increment_model.predict([50]), None)
            self.assertEqual(increment_model.predict([50, 52, 60]), 65)
            self.assertEqual(increment_model.predict([50, 52, 60, 65]), 70)
            self.assertEqual(increment_model.predict([0, 0, 0, 0]), 0)
            print('OK')
        except Exception as e:
            print('ho avuto un Errore Generico del tipo {}'.format(e))
"""
# test all
increment_model = FitIncrementModel()
#global_avg_increment = increment_model.fit([8, 19, 31, 41])
risultato = increment_model.predict([8, 19, 31, 41], [50, 52, 60])

print('{}'.format(risultato))

#chiamare unit test
#test_increment_model = TestIncrementModel()
#test_increment_model.TestIncrementModel()
