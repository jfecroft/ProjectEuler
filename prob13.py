"""
solution to project euler 13.
"""
FILE_NAME = 'prob13.txt'
NUMBER = 0

for line in open(FILE_NAME, 'r'):
    NUMBER += int(line)

print str(NUMBER)[0:10]
