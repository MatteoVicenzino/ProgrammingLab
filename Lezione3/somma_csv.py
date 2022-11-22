def sum_csv(file_name):
    elementi = []
    somma = 0.0
    file_sales = open(file_name, 'r')
    if file_sales == []:
        return None
    for line in file_sales:
        elementi = line.split(',')
        if elementi[0] != 'Date':
            valore = float(elementi[1])
            # print('{}'.format(valore))
            somma = somma + valore
    if somma == 0.0:
        return None
    return somma

# risultato = sum_csv('shampoo_sales.csv')
# print('{}'.format(risultato))

# per passare un file come argomento di una funzione devo mettere il nome tra apostrofi nelle chiamata