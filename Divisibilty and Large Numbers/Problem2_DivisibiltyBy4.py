'''A number is divisible by 4 if the last two numbers are divible by 4
For a number 12223856765023649236459258656 is 56 is divisble by 4 then we are done.
'''
n = 12345987868768269849287596521
i = 0 
num = 0
while i <2:
    remainder = n % 10
    n = n // 10
    num+= remainder * 10**i
    i +=1
if num % 4 ==0:
    print('Yes')
else:
    print('No')
    

#  Another Way without loop

def check(st): 
    n = len(st) 
  
    # Empty string 
    if (n == 0): 
        return False
  
    # If there is single 
    # digit 
    if (n == 1): 
        return ((st[0] - '0') % 4 == 0) 
  
   
    last = (int)(st[n - 1]) 
    second_last = (int)(st[n - 2]) 
  
    return ((second_last * 10 + last) % 4 == 0) 
  
  
# Driver code 
st = "76952"
  
# Function call 
if(check(st)): 
    print("Yes") 
else: 
    print("No ")
