import unittest

class Model():
    def fit(self, data):
        # Fit non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato') 
        
    def predict(self, data):
        # Predict non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
    def predict(self, data): 
        
        # check su data
        if type(data) is not list:
            raise Exception('data is not a list')
            return None
        if len(data) < 3:
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
        prediction = data[-1] + somma_incrementi/i
        return prediction


        # unit test
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

# test all
increment_model = IncrementModel()
print('{}'.format(increment_model.predict([50, 52, 60])))

#chiamare unit test
test_increment_model = TestIncrementModel()
test_increment_model.TestIncrementModel()
