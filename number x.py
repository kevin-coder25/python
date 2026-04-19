num = int (input("Enter a number:"))

list = (1,4,9,16,25,36,49,64,81,100)

len = len(list)

i = 0
while i < len:
    if list [i] == num:
        print ("FOUND at idx ", i)
        break
    else:
        print ("Not found")
    
    
    i += 1