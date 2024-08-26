import random

#random_number= random.randrange(-5, 11)
#randdom_number= random.randint(-5, 11) #now 11 will be included in the random number pool
top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please enter a number greater than zero: ")
        quit()
else:
    print("please enter a number next time")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please enter a number next time ")
        continue
    
    if user_guess == random_number:
        print("you got it! ")
        break
    elif user_guess > random_number:
            print("You were above the number!")
    else:
            print("You were below the number! ")
        

print("you got it in ", guesses, "guesses")