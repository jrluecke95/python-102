# getting user input for length of list here
while True:
    try:
        length = int(input("How long do you want your list to be? "))
        if length > 0:
            break
        else:
            False
    except ValueError:
        print("please enter a valid number")

for i in range(length):
    list_of_nums = [ ]
    try:
        num = int(input(f"What number do you want the {i + 1} item in the list to be? "))
    except ValueError:
        print("please enter a valid number")
    list_of_nums.append(num)

print(list_of_nums)