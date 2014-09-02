from PrimeFactorisation import PrimeFactors
import itertools
import numpy as np
from math import factorial

def GetCombinations(lst):  
 combs = []
 for i in xrange(1, len(lst)+1):
     els = [list(x) for x in itertools.combinations(lst, i)]
     combs.extend(els)
 return combs

def GenTri():
 i = 0
 Tri = 0
 while True:
  i   += 1
  Tri += i
  yield Tri


a = GenTri()

NumFactors = 0
while NumFactors < 500:
 TriNum  = a.next()
 Factors = PrimeFactors(TriNum)
 Combs = GetCombinations(Factors)
# print TriNum, len(Combs), factorial(len(Factors))
 Combs =[np.prod(i) for i in Combs] 
 NumFactors =  len(set(Combs))
# print TriNum, NumFactors, factorial(len(Factors))

print TriNum
