import math
import time
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
        time.sleep(0.5)
        print("Answer =", answer1)
        time.sleep(0.5)
        stepchoice = input ("Do you wish to see the working out?\n1 = Yes\n2 = No\nAnswer: ")

        if stepchoice == "1":
            print (num1, '² =' ,square1)
            print (num2, "² = ", square2,)
            print (square1, "+", square2, "=", add)
            print ("√", add, "=", answer1)
            restart = input("Do you wanna do another question? \n1 = Yes \n2 = No\nAnswer: ")
            if restart == "1":
                Pythagoras()
            elif restart == "2":
                print ("Okay")            

            
        elif stepchoice == "2":
            restart = input("Do you wanna do another question? \n1 = Yes \n2 = No\nAnswer: ")
            if restart == "1":
                Pythagoras()
            elif restart == "2":
                print ("Okay")





    elif choice == "2":
        numhigh = float(input("Enter the highest number of the two: "))
        numlow = float(input("Enter the lowest number of the two: "))
        square3 = math.pow(numhigh, 2)
        square4 = math.pow(numlow, 2)
        sub = square3 - square4
        answer2 = math.sqrt(sub)
        time.sleep(0.5)
        print ("Answer =", answer2)
        time.sleep(0.5)
        stepchoice2 = input ("Do you wish to see the working out?\n1 = Yes\n2 = No\nAnswer: ")
        if stepchoice2 == "1":
            print (numhigh, '² =' ,square3)
            print (numlow, "² = ", square4,)
            print (square3, "-", square4, "=", sub)
            print ("√", sub, "=", answer2)
            restart = input("Do you wanna do another question? \n1 = Yes \n2 = No\nAnswer: ")
            if restart == "1":
                Pythagoras()
            elif restart == "2":
                print ("Okay")            

            
        elif stepchoice2 == "2":
            restart = input("Do you wanna do another question? \n1 = Yes \n2 = No\nAnswer: ")
            if restart == "1":
                Pythagoras()
            elif restart == "2":
                print ("Okay")


Pythagoras()


