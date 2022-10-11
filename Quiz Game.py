print("Welcome To Quiz Game")

playing = input("Do You Want To Play? ")

if playing != "yes":
    quit()

print("Lets Start The Game")

Score = 0

answer1 = input("2 + 2 ")

if answer1 == "4":
    print("Correct")
    Score += 1

else:
    print("Incorrect")

answer2 = input("4 + 4 ")

if answer2 == "8":
    print("Correct")
    Score += 1

else:
    print("Incorrect")


answer3 = input("8 + 8 ")

if answer3 == "16":
    print("Correct")
    Score += 1

else:
    print("Incorrect")

print("You Got " + str(Score) + " Questions Correct!")
