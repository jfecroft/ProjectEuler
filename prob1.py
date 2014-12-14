UPPER_LIMIT = 1000

def multiple_of_three_or_five(num):
    if num%3 == 0:
        return True
    elif num%5 ==0:
        return True
    else:
        return False

sum = 0
for i in range(1,UPPER_LIMIT):
    if multiple_of_three_or_five(i): sum += i 

print sum 
