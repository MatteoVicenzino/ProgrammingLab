class Average():
    
    def mat_average(self, list):
        lunghezza = len(list)
        media = 0
        for i in range(lunghezza):
            media = media + list[i]
        return(media/lunghezza)

class MovingAverage(Average):
    
    def __init__(self, window):
        self.window = window

    def compute(self, list):
        result_list = [] #lista dei risultati che ritornerò
        lunghezza = len(list) - (self.window - 1)
        for i in range(lunghezza):
            #faccio un listina (di lunghezza window) con gli i-esimi window valori
            listina = []
            for j in range(self.window):
                listina.append(list[i+j])
            media_parz = self.mat_average(listina)
            result_list.append(media_parz)
        return(result_list)

# test all
moving_average = MovingAverage(2)
result = moving_average.compute([2, 4, 8, 16])
print(result)