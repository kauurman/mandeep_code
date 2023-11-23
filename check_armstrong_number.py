num = int(input("enter the number here:"))
sum = 0 
temp = num 
while temp > 0:
    digit = temp% 10 
    cube = digit **3 
    sum = sum + cube 
    temp //= 10

if sum == num:
    print ('it is an armstrong numer')

else: 
     print ('it is not a armstrong number') 
        
