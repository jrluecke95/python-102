list1 = [[1, 3], [2, 4]]
list2 = [[5, 2], [1, 0]]

new_list = [[],[]]

for i in list1:
    for j in i:
        new_list[0] = list1[i] + list2[j]

print(new_list)




#print(list1[0][0]) = 1