a = 48
b = 18

def GCDUsigEuclidean(a,b):
  while b !=0:
    a , b = b , a % b

  return a

print(GCDUsingEuclidean(a,b))
