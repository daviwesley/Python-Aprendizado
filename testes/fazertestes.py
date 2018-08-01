import unittest

def fibo(n):
   if n < 2:
      return n
   else:
      return fibo(n-1) + fibo(n-2)
 
class testa_fibonacci(unittest.TestCase):
   def teste_um(self):
      self.assertEqual(fibo(0),0)
 
   def teste_dois(self):
      self.assertEqual(fibo(1),1)
 
   def teste_tres(self):
      self.assertEqual(fibo(7),13)
 
   def teste_quatro(self):
      self.assertEqual(fibo(10),55)
 
unittest.main()
