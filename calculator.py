num1 = int (input ("Enter a number: "))
num2 = int (input ("Enter a number: "))

ch =  (input ("Select an operator (+, - , * , /)"))

if (ch == "+"):
    print ("Addition = ", num1 + num2)
elif (ch == "-"):
    print ("Subtraction = ", num1 - num2)
elif (ch == "*"):
    print ("Multiplication = ", num1 * num2)
elif (ch == "/"):
    if (num2 == 0):
        print ("Division by zero is not possible")
    else:
        print ("Division = ", num1 / num2)