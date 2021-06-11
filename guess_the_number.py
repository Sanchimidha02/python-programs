#guess the number game using python
print("let's start the game!")
print("Tip: you will get only 10 chances")
n=30 #actual number
chances=1 #no of chances
while(chances<=10):
    guess_the_number= int(input("Guess the number:\n"))
    if(guess_the_number<30):
        print("you entered less number ,input greater number ")
    elif(guess_the_number>30):
        print("you entered greater number ,input lesser number ")
    else:
        print("YOU WON!!")
        print(chances, "no.of guesses you took to finish.")
        break
    print(10 - chances, "guesses left")
    chances = chances + 1

if (chances > 10):
    print("Game Over:)")
