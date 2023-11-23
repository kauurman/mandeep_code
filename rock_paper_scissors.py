import random
print ("~~~~~~~~~~~~~~~~~~~~~ welcome to RPS~~~~~~~~~~")
user_score = 0 
comp_score = 0 
ties = 0

name = input ("enter your name here: ")
print(""" 
Winning Rules:
1.Paper VS Rock --> Paper 
2. Rock VS Scrissors --> Rock 
3. Scissors VS Paper --> Scissors""")

print () 
print (""" Choices are:
1. Rock 
2. Paper
3. Scrissors""")

choice = input("enter your choice from 1-3:") 
print()

while choice > 3 or choice < 1 : 
    choice = int(input("enter valid inport"))
if choice == 1:
    user_choice = "Rock"
elif choice == 2: 
    user_choice = "Paper " 

else:
    user_choice =="scissors"

print ("The user's choice is",user_choice)
print ("Now it is computer's trun")
computer = random.randint(1,3)
if computer == 1:  
    comp_choice = "Rock" 
elif computer == 2:
    comp_choice = "Paper" 
else:
    comp_choice = "Scrissors"

print ("The computer's choice is", comp_choice) 
if ((user_choice == "paper" and comp_choice == "Rock") or (user_choice == "Rock " and comp_choice == "paper")):
    print ("paper wins")
    result = "paper"

elif ((user_choice == "scissors" and comp_choice == "Rock") or (user_choice == "Rock " and comp_choice == "paper")):
    print ("Rock wins")
    reslut = "Rock"

elif (user_choice == comp_choice):
    print ("it's a tie") 
    reslut = "Tie" 


else: 
    print ("scissors wins")
    result = " scissors "

if result == "Tie" 
   ties += 1 
elif result == user_choice: 
    user_score += 1 
else:
    comp_score += 1 
    print ("scores are ")

print  (name "'s score is", user_score)
print ("computer 's score is", comp_score)
print ("ties are ",ties) 

repeat = input ("do you want to you again?")

if repeat == "no" or repeat == "no"
        
 break 
    
print ("game over!")
print ('Thank for playing !!!')

