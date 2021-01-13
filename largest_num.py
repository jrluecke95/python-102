while True:
    try:
        num1 = int(input("What is the first number in your range? "))
        break
    except ValueError:
        print("please select a valid number")
while True:
    try:
        num2 = int(input("What is the second number in your range "))
        break
    except ValueError:
        print("please select a valid number")

list_of_nums = list(range(num1, num2 + 1))
large_num = 0

for i in list_of_nums:
    if i > large_num:
        large_num = i

print(large_num)
