import random
randNum = int(random.randint(1,100))
guesses = 0 
user = input("Enter Your Name: ")
userGuess=None
while(randNum!=userGuess):
    userGuess = int(input("Enter a number: "))
    guesses+=1
    if(userGuess==randNum):
        print("You guessed it right!!!")
    else:
        if(userGuess<randNum):
            print("A higher Number please!!!")
        else:
            print("A small Number please!!!")
    

print(f"You guessed in {guesses} guesses!!!")

with open("highestScore.txt","r") as f:
    # f.readline()
    # hiscore = int(f.readline())
    lineNum = 2
    lines = f.readlines()
    # print(lines)
    if lineNum <= len(lines):
        specificLine = lines[lineNum-1]
        hiscore = int(specificLine)
        # print(specificLine)
    else:
        print("line out of range")
    # print(hiscore)

if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("highestScore.txt", "w") as f:
        message=f"{user} has the higest Score\n{str(guesses)}"
        f.write(message)
        
# with open("hiscore.txt", "r") as f:
#     hiscore = int(f.read())
# if(guesses<hiscore):
#     print("You have just broken the high score!")
#     with open("hiscore.txt", "w") as f:
#         f.write(str(guesses))