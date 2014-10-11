from PrimeFactorisation import ProperDivisors
import numpy as np

def d(n):
 PD = np.array(list(ProperDivisors(n)))
 return np.sum(PD)

low, high = 2, 10000  #start at 2 to avoid empty set for proper divisors for 1
sum_divisors = [d(n) for n in xrange(low,high+1)] #get d(n)  for n

sum = 0 
for i, j  in enumerate(sum_divisors):
  if i+low < j and j-low >= 0 and j-low <= len(sum_divisors)-1 and sum_divisors[j-low] == i+low:
   sum += i+low 
   sum += j 

print sum
