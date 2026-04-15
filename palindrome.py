list = [1,2,3,2,1]

copy_list = list.copy()
copy_list.reverse()

if (copy_list == list):
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")