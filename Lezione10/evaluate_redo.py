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

    def __init__(self, data_fit, data_evaluate, window):
        self.data_fit = data_fit
        self.data_evaluate = data_evaluate
        self.window = window
    
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
        for i in range(lunghezza - 4):
            predizione = self.predict([data[i], data[i+1], data[i+2]])
            errore = data[i+4] - predizione
            count = count+1
            if errore < 0:
                errore_medio = errore_medio - errore
            else:
                errore_medio = errore_medio + errore
        return errore_medio/count

class FitIncrementModel(IncrementModel):
    
    def fit(self, data):
        return self.media_incrementi(data) 
        
    def predict(self, data1, data2):
        fitted = self.fit(data1)
        predicted = self.media_incrementi(data2)
        return (data2[-1] + (fitted + predicted)/2)

    
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


increment_model = IncrementModel()
risultato_i = increment_model.evaluate([67, 72, 72], 3)
print('errore medio senza fit: {}'.format(risultato_i))

fit_increment_model = FitIncrementModel()
risultato_f = fit_increment_model.evaluate([8, 19, 31, 41, 50, 52, 60], [67, 72, 72], 3)
print('errore medio con fit: {}'.format(risultato_f))