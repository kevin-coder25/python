num1 = int (input ("Enter first number: "))
num2 = int (input ("Enter second number: "))
num3 = int (input ("Enter third number: "))

greater = num1

if (num2 > greater):
    greater = num2
if (num3 > greater):
    greater = num3

print ("Greatest number = ", greater)

