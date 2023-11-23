# this library is use to import the random numbers float and character values
import random 


#list of character is intialized whose name is words
words = ["iranman"," thor", "hawkeye","wanda", " vision" ]
#list of character is  random choice words and print 
word = random . choice (words)
print (word)
# list  character use by jumble  word and print 
jumble = " ".join(random.sample (word,len (word )))
print(jumble)

#list of character use to use to   chances and print and name is words  avengers jumble bumble 
chances = 4 
print ("~"*30 )
print ("~~~~~ Avengers Jumble Bumble ~~~~~~")
# list of character use to while , print and character input , lower 
while chances!= 0: 
    print ("the word is", jumble )
    guess = input("enter your gussed word:").lower()
# list of character  use to if , print and word and break 
    if guess == word:
        print ("corred guess!!")
        print ("you won!!")
        break     
    #list of character use to else , chances and print 
    else: 
        chances -= 1 
    print ("Incorrect guess!")
    print("Remaning chances are:", chances )
 #list of character use to else and print 
else: 
    print("all you chances are exhasted ")
    print ("you lose ")
    print ("the correct word is word")
    print ("thank you for playing ")
