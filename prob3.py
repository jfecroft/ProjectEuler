from math import sqrt
Prime = 42000
Prime = 600851475143
Prime = Prime*9233
Prime = 35


def prime(n):
  i=2
  while (n%i != 0 and i < n):
    i += 1
    print n,i,n%i
  if (i < n):
    return prime(n/i)
  else:
    print("The highest prime factor is: "),n

prime(Prime)
