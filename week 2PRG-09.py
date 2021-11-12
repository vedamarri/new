import random
n = random.randrange(1,99)
guess = int(input ("Enter an integer from 1 to 99:"))
while guess!= n:
    if guess<n:
        print ("guess higher.Try again")
        guess = int(input("Enter an integer from 1 to 99:"))
    else:
        print ("guess lower.Try again")
        guess = int(input("Enter an integer from 1 to 99:"))
print("You guessed it correct!")
