import random 
random_number=random.randint(1,10)
while True:
     guess=int(input("enter a number between 1 and 10"))
     if guess < random_number:
           print("TOO LOW!")
     elif guess > random_number:
           print("TOO HIGH!") 
     else :
           print("YOU WON BROOOOOOO!!!!!!!")
           play_again=input("do you want to play again? (y/n)")
           if play_again== "y":
           	    random_number=random.randint(1,10)
           	    guess= None
           else:
           		print("Thank you for playing!")
           		break

    