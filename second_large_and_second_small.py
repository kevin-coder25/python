ls_num = []
num = int (input("Enter a number:"))
ls_num.append(num)
num = int (input("Enter a number:"))
ls_num.append(num)
num = int (input("Enter a number:"))
ls_num.append(num)

greater = ls_num[0]
smallest = ls_num[0]
#for greater
if (ls_num[1] > greater and ls_num[1] > ls_num[2]):
    greater = ls_num[1]
elif (ls_num[2] > greater and ls_num[2] > ls_num[1]):
    greater = ls_num[2]
#for smallest
if (ls_num[1] < smallest and ls_num[1] < ls_num[2]):
    smallest = ls_num[1]
elif (ls_num[2] < smallest and ls_num[2] < ls_num[1]):
    smallest = ls_num[2]
#second largest
if (ls_num[1] > ls_num[2] and ls_num[1] < greater):
    second_largest = ls_num[1]
elif (ls_num[2] > ls_num[1] and ls_num[2] < greater):
    second_largest = ls_num[2]
#second smallest
if (ls_num[1] < ls_num[2] and ls_num[1] > smallest):
    second_smallest = ls_num[1]
elif (ls_num[2] < ls_num[1] and ls_num[2] > smallest):
    second_smallest = ls_num[2]

print("The greatest number is:", greater)
print("The second greatest number is: ", second_largest)
print("The smallest number is:", smallest)
print("The second smallest number is: ", second_smallest)

