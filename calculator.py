class calculator:
 def __init__(self,a,b):
  self.a=a
  self.b=b
 def sum(self):
  sum1=self.a+self.b
  return sum1
 def subtraction(self):
  subtract=self.a-self.b
  return subtract
 def multiplication(self):
  multi=self.a*self.b
  return multi
 def division(self):
  divi=self.a/self.b
  return divi
 
calci=calculator(6,7)
print(f"sum of two numbers is {calci.sum()} ")
print(f"subtraction of two numbers is {calci.subtraction()}")
print(f"multiplication of two numbers is {calci.multiplication()}")
print(f"division of two numbers is {calci.division()} ")