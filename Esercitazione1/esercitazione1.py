class ExamException(Exception):
        pass

class Average():
    
    def mat_average(self, lista):
        lunghezza = len(lista)
        media = 0
        for i in range(lunghezza):
            media = media + lista[i]
        return(media/lunghezza)

class MovingAverage(Average):
    
    def __init__(self, window):
        self.window = window
        
        #controlli su window
        if type(self.window) is not int:
            raise ExamException('la finestra deve essere un intero')
        if self.window < 1:
            raise ExamException('la finestra almeno 1')

    def compute(self, lista):

        #controlli su lista
        if (lista == None) or (lista == []):
            raise ExamException('lista non definita')
        if type(lista) is not list:
            raise ExamException('no è stata fornita una lista')
        if self.window < 1:
            raise ExamException('la finestra almeno 1')
        for item in lista:
            if (type(item) is not int) and (type(item) is not float):
                raise ExamException('gli elementi delle lista devono essere numeri')
        if self.window > len(lista):
            raise ExamException('la finestra è più grande della lista')

        
        result_list = [] #lista dei risultati che ritornerò
        lunghezza = len(lista) - (self.window - 1)
        for i in range(lunghezza):
            #faccio un listina (di lunghezza window) con gli i-esimi window valori
            listina = []
            for j in range(self.window):
                listina.append(lista[i+j])
            media_parz = self.mat_average(listina)
            result_list.append(media_parz)
        return(result_list)

        
# test all
moving_average = MovingAverage(2)
result = moving_average.compute([2, 4, 8, 16])
print(result)