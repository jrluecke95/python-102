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

# creating list
list_of_nums = [ ]

# looping through list asking for numbers that the user wants to put in
for i in range(length):
    try:
        num = int(input(f"What number do you want the {i + 1} item in the list to be? "))
    except ValueError:
        print("please enter a valid number")
    list_of_nums.append(num)
    
# looping through list, starting with first number, finding smallest
for i in list_of_nums:
    small_num = list_of_nums[0]
    if i < small_num:
        small_num = i

print(small_num)