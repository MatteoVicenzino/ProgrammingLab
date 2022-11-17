#definisco una funzione sum_list che prende in entrata una lista di numeri e li somma
def sum_list(mylist):
    risultato = 0
    for item in mylist:
        risultato = risultato + item
    if mylist == []:
        return None
    return risultato
    