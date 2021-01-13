list1 = [2, 4, 5]
list2 = [2, 3, 6]

new_list = []

ind = 0
for i in list1:
    new_list.append(i * list2[ind])
    ind += 1

print(new_list)