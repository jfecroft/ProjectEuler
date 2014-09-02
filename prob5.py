import math
def is_prime(n):
    if n%2 == 0 and n > 2: 
        return False
    return all(n%i for i in range(3, int(math.sqrt(n)) + 1, 2))

def is_multiple(n,nums):
 return all(n%i == 0 for i in nums)

NumMax = 20
PrimesList = []
for i in range(2,NumMax):
 if is_prime(i): PrimesList.append(i)

i = NumMax
while not is_multiple(i,range(1,NumMax+1)):
 i += NumMax
# if is_multiple(i,PrimesList):
#  print i, is_multiple(i,range(1,NumMax)),is_multiple(i,PrimesList)



print i
