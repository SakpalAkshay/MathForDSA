'''
Naive approach: A simple method is repeated subtraction. 
Following is another interesting method.
Divisibility by 7 can be checked by a recursive method. 
A number of the form 10a + b is divisible by 7 if and only if 
a – 2b is divisible by 7. In other words, subtract twice the last digit from the number formed by the remaining digits.
Continue to do this until a small number. 
'''


#Naive Approach - Repeated Subtraction

n = 350
isDivisible = False
while n > 0:
    n = n - 7
    
    if n == 0:
        isDivisible = True

if isDivisible:
    print("Yes")
else:
    print("No")
    
#recursive approach

def isDivisibleBy7(n):
    
    # if number becomes - negative in recursive case make it positive
    if n < 0:
        return isDivisibleBy7(-n)
    
    #base case
    if (n==0 or n==7):
        return True
    
    if n<10:
        return False
    #make a - 2b format
    return (n//10 - 2*(n-n//10*10))

if isDivisibleBy7(n):
    print("Yes")
else:
    print("No")
