import itertools
from collections import deque

def IsPalindrome(String):
 character_deque = deque()
 #put all chracters in deque then check one by one
 for i in String: character_deque.appendleft(i)

 Equal = True
 while Equal and len(character_deque) > 1:
  rightcharacter = character_deque.pop()
  leftcharacter  = character_deque.popleft()
  if rightcharacter != leftcharacter: Equal = False #if any not equal then not a palidrome
 return Equal

NumMax = 999
Highest = 0
for i,j in itertools.product(range(NumMax+1),range(NumMax+1)):
 if IsPalindrome(str(i*j)) and i*j > Highest:
  Highest = i*j


print Highest
