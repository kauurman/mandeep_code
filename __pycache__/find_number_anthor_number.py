
#print ("the number divisible by 13 are:")

#for i in range (1,100):
    #if i % 13 == 0:
        #print (i)

#solution2 
l  = ["39,48,26,98,33,67,87"]

result =  list(filter(lambda X : X% 13 == 0,l))
print ('the number divisible by 13 are',result) 