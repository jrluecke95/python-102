print("hello there! this program will reverse any combination of letters, numbers, and words you like!")
string = input("What would like to reverse today? ")

string_list = list(string)

reverse_list = []
pos = -1
for i in string_list:
    reverse_list.append(string_list[pos])
    pos -= 1

reverse_string = "".join(reverse_list)
print(reverse_string)