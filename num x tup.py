num = int (input("Enter a number:"))

list = (1,4,9,16,25,36,49,64,81,100)
idx = 0
for val in list:
    if (val == num):
        print("Found", idx)
        break
    idx += 1