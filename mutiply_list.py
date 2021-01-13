# letting the user determine the length of thir list and what factor they want to multiply it by
while True:
    try:
        factor = int(input("What number do you want to multiply your list by? "))
        break
    except ValueError:
        print("please enter a valid number")
while True:
    try:
        length = int(input("How long do you want your list to be? "))
        if length > 0:
            break
        else:
            False
    except ValueError:
        print("please enter a valid number")

#creating a for loop for the user to add numbers to the list
list_of_nums = [ ]
for i in range(length):
    try:
        num = int(input(f"What do you want the {i + 1} number in your list to be? "))
    except ValueError:
        print("please enter a valid number")
    list_of_nums.append(num)

multi_list = [ ]
counter = 0
while counter < len(list_of_nums):
    multi_list.append(list_of_nums[counter] * factor)
    counter += 1

print(multi_list)