#definisco una funzione sum_list che prende in entrata una lista di numeri e li somma
def sum_list(mylist):
    risultato = 0
    for item in mylist:
        risultato = risultato + item
    return risultato

mylist = [0,0,0]
if mylist == []:
    somma = None
else:
    somma = sum_list(mylist)
print('La somma dei valori è: {}'.format(somma))