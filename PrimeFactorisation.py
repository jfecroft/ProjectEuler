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
