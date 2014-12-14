FILE_NAME = 'prob13.txt'
num = 0

for line in open(FILE_NAME, 'r'):
    num += int(line)

print str(num)[0:10]
