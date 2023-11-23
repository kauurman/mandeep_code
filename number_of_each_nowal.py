#a = "Harry potter and the Prisoner of Azkaban"

#vowels = "aeiou"

#a = a.casefold()

#print (a)

#count = {}. fromkeys(vowels,0)

#for char in a :

    #if char in count :
        #count [char]+= 1 
#print (count)




solution2 

a = "Harry Potter and the Prisoner of Azkaban"
vowels = "aeiou"

a = a. casefold()

count = {key: sum([1 for char in a if char == key ]) for key in vowels }

print(count) 

