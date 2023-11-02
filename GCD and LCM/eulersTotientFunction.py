n = 10

def gcd(a,b):
    while b!=0:
        a,b = b, a%b
    return a

relativleyPrimeNumbers = []
for i in range(1,n):
    GCD = gcd(i,n)
    
    if GCD == 1:
        relativleyPrimeNumbers.append(i)


print(relativleyPrimeNumbers)
