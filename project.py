'''The task is to create a script that generates  a random number between a fixed range,and if the user guesses the number right in three chances ,then user wins otherwise user lose.This game user can play as many numbers of times and whenever user wins a score is to be given to the user.At the
 end the usersscore must be displayed on the screen.Hint: Make use of random module to design the game Abstract steps:
 1.The user enters the  lower  and upper bounds of the range .
2. As a result , the compiler generates a random integer between the range and stores it in a  variable for future use .
3.A while loop will be created for repetitive guessing.
4.When a user guesses a number that is graeter than a randomly selected number ,the user grecieves the message"have one more try".Your guess was too high .
if the user guesses a number that is graeter than a randomly selected number ,the user recieves the message"have one more try".Your guess was too high .hasattrIf the user guesses a number smaller than a randomly selected number , the user gets an output of"have one more try"."Your guess was too small. "
if the user gets an output of "have one more try".your guess was too small." '''




import random
s,e=int(input("starting range: ")),int(input("ending range: "))
score=0
while True:
    number=random.randint(s,e)
    for i in range(1,4):
        print("(TRY ",i,") guess the number: ",sep="",end="")
        u_input=int(input())
        if u_input>number:
            print("TRY AGAIN --- guessed higher")
        elif u_input<number:
            print("TRY AGAIN --- guessed smaller")
        else:
            print("congrats right guess")
            score+=1
            break
    print("The number was",number)
    print("current score is =",score)
    repeat=input("another round? N/Y: ")
    if repeat=="N":
        break
print("your final score is",score)