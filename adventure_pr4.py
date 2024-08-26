name = input("Type your name: ")
print("Welcome!", name, "to this adventure!")

answer = input(
    "You are on the dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()


if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim ot swim across: ").lower()
    if answer == "swim":
        print()
    elif answer == "walk":
        print()
    else:
        print("Not an valid option, You lose!")
elif answer == "right":
    print()

else:
    print("Not an valid option, You lose!")