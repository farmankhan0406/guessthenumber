n=20
guess=0
while(guess<9):
    print("Guess the number")
    num=int(input())

    if(num==n):
        print("you guessed the correct number\n")
        print("gameover")
        break
    elif(num<n):
        print("you entered the smaller number\n")
        print("number of guess left=", 8 - guess)
        if(guess==9):
            print("game over")
    elif(num>n):
        print("you entered the greater number\n")
        print("number of guess left=", 8 - guess)
        if (guess == 8):
            print("game over")

    guess=guess+1


