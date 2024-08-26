print("Welcome to my computer quiz!")

playing = input("do you want to play? ")

if playing.lower()!= "yes":
    quit()

print("Okay! Let's play :)")
score = 0;
answer = input("what does cpu stand for? ").lower()
if answer== "central processing unit":
    print("Correct!")
    score+=1;
else:
    print("Incorrect!")

answer = input("what does gpu stand for? ").lower()
if answer== "graphics processing unit":
    print("Correct!")
    score+=1;
else:
    print("Incorrect!")

answer = input("what does ram stand for? ").lower()
if answer== "random access memory":
    print("Correct!")
    score+=1;
else:
    print("Incorrect!")

answer = input("what does psu stand for? ").lower()
if answer== "power supply unit":
    print("Correct!")
    score+=1;
else:
    print("Incorrect!")

print("You got "+ str(score) + " questions correct! ")
print("You got "+ str((score/4)*100) + " Percent! ")