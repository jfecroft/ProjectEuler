UpperLimit = 1000

def MultipleOfThreeOrFive(num):
 if num%3 == 0:
  return True
 elif num%5 ==0:
  return True
 else:
  return False


sum = 0
for i in range(1,UpperLimit):
 if MultipleOfThreeOrFive(i): sum += i 


print sum 
