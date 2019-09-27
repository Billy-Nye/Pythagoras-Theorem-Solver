import math
print ("Pythagoras Theorem solver for different sides of the triangle \n")

def Pythagoras():
    choice = input("Which one you doing? Hypotenuse, the one opposite to the 90° angle? or the ones next to the 90° angle? \n1 = Hypotenuse \n2 = Others \nAnswer = ")

    if choice == "1":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        square1 = math.pow(num1, 2)
        square2 = math.pow(num2, 2)
        add = square1 + square2
        answer1 = math.sqrt(add)
        print (answer1)
        restart = input("Do you wanna do another question? \ny = Yes \nn = No\nAnswer: ")
        if restart == "y":
            Pythagoras()
        elif restart == "n":
            print ("Okay")





    elif choice == "2":
        numhigh = float(input("Enter the highest number of the two: "))
        numlow = float(input("Enter the lowest number of the two: "))
        square3 = math.pow(numhigh, 2)
        square4 = math.pow(numlow, 2)
        sub = square3 - square4
        answer2 = math.sqrt(sub)
        print (answer2)
        restart = input("Do you wanna do another question? \ny = Yes \nn = No\nAnswer: ")
        if restart == "y":
            Pythagoras()
        elif restart == "n":
            print ("Okay")


Pythagoras()


