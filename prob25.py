
def fib():
 a,b = 0,1
 while True:
  a,b = b,a+b
  yield b

NumDigits = 3
NumDigits = 1000

FibGen = fib()
FibNum = 0
term = 1
while len(str(FibNum)) < NumDigits:
 FibNum = FibGen.next()
 term += 1

print term 
 
