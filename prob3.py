from math import sqrt
Prime = 42000
Prime = 600851475143


def prime(n):
  i=2
  while (n%i != 0 and i < n):
    i += 1
  if (i < n):
    return prime(n/i)
  else:
    print n

prime(Prime)
