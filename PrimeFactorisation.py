def PrimeFactors(n,PrimesList=None):
  """returns the prime factorisation of n"""
  if PrimesList == None: PrimesList = []
  i=2
  while (n%i != 0 and i < n):
    i += 1
  if i > 1:PrimesList.append(i)
  if (i < n):
    return PrimeFactors(n/i,PrimesList)
  else:
    PrimesList.append(1)
    return PrimesList

def PrimesLessThanN(NumMax):
 PrimesList =[]
 Primes = [True]*NumMax
 i=2
 while i < sqrt(NumMax):
  if Primes[i] is True:
   j = i**2
   while j < NumMax:
    Primes[j] = False
    j += i
  i += 1

 for i in range(2,len(Primes)):
  if Primes[i] == True: PrimesList.append(i)
 return PrimesList
