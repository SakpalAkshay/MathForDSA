'''A number is divisible by 6 it's divisible by 2 and 3. 
a)  A number is divisible by 2 if its last digit is divisible by 2.
b)  A number is divisible by 3 if sum of digits is divisible by 3.'''

n = 47378707960746

count = 0

forTwo = 0
forThree = 0
while n>0:
    
    count+=1
    remainder = n % 10
    if count == 1:
        forTwo = remainder
    forThree+= remainder
    n = n //10

if(forTwo % 2 ==0 and forThree % 3 ==0):
    print("Yes")
else:
    print("No")
    
