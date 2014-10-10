from PrimeFactorisation import ProperDivisors
import numpy as np

def d(n):
 PD = np.array(list(ProperDivisors(n)))
 return np.sum(PD)

low, high = 2, 10000  #start at 2 to avoid empty set for proper divisors for 1
sum_divisors = [d(n) for n in xrange(low,high+1)] #get d(n)  for n

pairs=[]
for i in range(high-low+1):
 ind = sum_divisors[i] #index to compare to
 if i + low < ind and ind <= high and sum_divisors[ind - low] == i + low:
  pairs.append([i+low,ind])


print np.sum(np.array(pairs))
