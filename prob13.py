FILE_NAME = 'prob13.txt'
number = 0

for line in open(FILE_NAME, 'r'):
    number += int(line)

print str(number)[0:10]
