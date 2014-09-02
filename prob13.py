import numpy as np
import decimal
filen = 'prob13.txt'
num = 0
for line in open(filen,'r'):
 num += int(line)

print str(num)[0:10]
