import math

n = int(input())
print("Juggler series is as follows")
print(n, end ="")
while n != 1:
  b = 0 
  if n % 2 ==0:
    b = (int)(math.floor(math.sqrt(a)))
  else: 
    b = (int)(math.floor(math.sqrt(a) * math.sqrt(a) * math.sqrt(a) ) )
  print(b, end="")
  n = b 
  
  
