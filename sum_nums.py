while True:
    try:
        user_num1 = int(input("What is the first number of the range of numbers you want to add up? "))
        break
    except ValueError:
        print("Please select a valid number")
while True:
    try:
        user_num2 = int(input("What is the second number of the range of numbers you want to add up? "))
        break
    except ValueError:
        print("Please select a valid number")

list_of_nums = list(range(user_num1, (user_num2 + 1)))

sum = 0
for i in list_of_nums:
    sum += i

print(sum)

