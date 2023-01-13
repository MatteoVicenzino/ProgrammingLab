class ExamException(Exception):
        pass

class Diff():
    
    def __init__(self, ratio=1):
        self.ratio = ratio
        
        #controlli su ratio
        if type(self.ratio) is not int and type(self.ratio) is not float:
            raise ExamException('il rapporto deve essere un intero')
        if self.ratio < 1:
            raise ExamException('il rapporto deve essere almeno 1')

    def compute(self, lista):

        #controlli su lista
        if (lista == None) or (lista == []):
            raise ExamException('lista non definita')
        if type(lista) is not list:
            raise ExamException('non è stata fornita una lista')
        if len(lista) < 2:
            raise ExamException('la lista deve avere almeno due elementi')
        if self.ratio < 1:
            raise ExamException('il divisore deve essere almeno 1')
        for item in lista:
            if (type(item) is not int) and (type(item) is not float):
                raise ExamException('gli elementi delle lista devono essere numeri')
        #if self.ratio > len(lista):
            #raise ExamException('la finestra è più grande della lista')

        
        result_list = [] #lista dei risultati che ritornerò
        lunghezza = len(lista)
        for i in range(lunghezza - 1): #le differenze tra l elementi sono l-1
            differenza = lista[i+1] - lista[i]
            result_list.append(differenza/self.ratio)
        return(result_list)

        
# test all
diff = Diff()
result = diff.compute([2,4,8,16])
print(result) # Deve stampare a schermo [2.0,4.0,8.0]