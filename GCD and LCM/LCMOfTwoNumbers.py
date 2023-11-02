a = 4
b = 9

def gcd(a,b):
    
    while b!=0:
        a,b = b, a % b
    return a



def lcm(a,b):
    GCD = gcd(a,b)
    
    return (a * b) // GCD

LCM = lcm(a,b)

print(LCM)
