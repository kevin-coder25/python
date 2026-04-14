num1 = int (input ("Enter first number : "))
num2 = int (input ("Enter second number : "))
num3 = int (input ("Enter third number : "))
num4 = int (input ("Enter forth number : "))

greater = num1

if (num2 > greater and num2 > num3 and num2 > num4):
    greater = num2
elif (num3 > greater and num3 > num2 and num3 > num4):
    greater = num3
elif (num4 > greater and num4 > num3 and num4 > num2):
    greater = num4

print ("Greater number = ", greater)