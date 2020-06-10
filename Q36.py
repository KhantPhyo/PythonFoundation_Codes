inputItems = input("Please enter your lists (number only) : ")
userList = inputItems.split(',')
sum_numbers = 0

for x in userList:
    sum_numbers += int(x)

print("Sum of your list is : ", sum_numbers)
