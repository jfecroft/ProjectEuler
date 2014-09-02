
NumMax =1000 

for a in xrange(1,NumMax):
 for b in xrange(a,NumMax-a+1):
  c = NumMax -a -b
  if a**2+b**2 == c**2:print a*b*c
