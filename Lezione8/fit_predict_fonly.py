class Model():
    def fit(self, data):
        # Fit non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato') 
        
    def predict(self, data):
        # Predict non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
    def predict(self, data): 
        # checks non implementati
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
