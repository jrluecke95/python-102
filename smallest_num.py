while True:
    try:
        length_of_list = int(input("How long do you want your list to be? "))
        if length_of_list > 0:
            break
        else:
            
    except ValueError:
        print("please enter a valid number")

# print(small_num)