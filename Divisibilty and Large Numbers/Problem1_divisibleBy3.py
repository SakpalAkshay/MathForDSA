'''A number is divisible by 3 if sum of its digits is divisible by 3.'''

def checkDiv(num) : 
	
	# Compute sum of digits 
	digitSum = 0
	while num > 0 : 
		rem = num % 10
		digitSum = digitSum + rem 
		num = num // 10
		
	# divisible by 3. 
	return (digitSum % 3 == 0) 
	
num = 1332
if(checkDiv(num)) : 
	print ("Yes") 
else : 
	print ("No") 
