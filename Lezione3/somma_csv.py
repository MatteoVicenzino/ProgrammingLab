def sum_csv(sales):
    elementi = []
    somma = 0.0
    for line in sales:
        elementi = line.split(',')
        if elementi[0] != 'Date':
            
            valore = float(elementi[1])
            # print('{}'.format(valore))
            somma = somma + valore
    return somma


sales = open('shampoo_sales.csv' , 'r')
risultato = sum_csv(sales)
print('{}'.format(risultato))
sales.close