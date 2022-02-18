import random
randomNumber = random.randint(1,100)
# print(randomNumber)
userGuess = None
guesses = 0
while(userGuess != random):
    userGuess = int(input("Enter Your guess :"))
    guesses +=1
    if(userGuess == randomNumber):
        print("\n      Right Guess!! \n *****CONGRATS YOU WIN*****")
        break
    else:
        if(userGuess > randomNumber):
            print("Wrong Guess!! Please try Smaller number")    
        else:
            print("Wrong Guess!! Please try Larger number")
    
print(f"You guessed the number in {guesses} guesses.")
print("\n Want to Play Again!!")            

# To store High Score in file
with open("HighScore.txt") as f:
    highscore = int(f.read())
    
if(guesses < highscore):
    print("*****HURRAY!!******\nYou have just broken High Score !! ")
    with open("HighScore.txt","w") as f:
        f.write(str(guesses))    
