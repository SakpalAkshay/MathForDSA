'''
A number is divisible by 11 if difference of following two is divisible by 11. 

Sum of digits at odd places.
Sum of digits at even places.
'''


n = '699210933779831'
oddSum = 0
evenSum = 0
for i in range(0,len(n)):
    
    if i % 2 ==0:
        evenSum += int(n[i])
    else:
        oddSum+= int(n[i])
        


if ((oddSum - evenSum)%11 ==0 ):
    print("Yes")
else:
    print("No")
    

