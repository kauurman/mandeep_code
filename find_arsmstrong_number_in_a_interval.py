lower  = int(input("enter the lower limit here:"))
upper = int(input("enter thr upper limit here:"))

sum = 0
for num in range (lower,upper + 1):
     order = len(str(num))

temp = num 
while temp > 0: 
    digit = temp % 10 
    sum += digit ** order 
    temp //= 10  
if num == sum:
    print (num)


