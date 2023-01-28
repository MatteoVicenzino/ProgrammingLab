import unittest

class Calcolatrice:
    
    def somma():
    def sottrazione():
    def moltiplicazione():
    def divisione():
    def potenza():
    def modulo():
    def radice():
    def cambio_base():

class TestCalcolatrice(unittest.testcase):
    
    def test_calcolatrice(self):
        try:
            calcolatrice = Calcolatrice()
            
            #se non ci sono input l'autput deve essere None
            self.assertEqual(calcolatrice.somma(), None)
            self.assertEqual(calcolatrice.sottrazione(), None)
            self.assertEqual(calcolatrice.moltiplicazione(), None)
            self.assertEqual(calcolatrice.divisione(), None)
            self.assertEqual(calcolatrice.potenza(), None)
            self.assertEqual(calcolatrice.modulo(), None)

            #test richiesti
            
            #test per provare
            self.assertEqual(calcolatrice.somma(2, 3), 5)
            
        except Exception as e:
            print("Ho avuto un errore del tipo {}".format(e))


#chiamare test
test = TestCalcolatrice()
test.test_calcolatrice()