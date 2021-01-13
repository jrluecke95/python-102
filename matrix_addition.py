list1 = [[1, 3], [2, 4]]
list2 = [[5, 2], [1, 0]]

new_list = [[0, 0], [0, 0]]

for i in range(len(list1)):
    for j in range(len(list1[0])):
        new_list[i][j] = list1[i][j] + list2[i][j]
    

print(new_list)




#print(list1[0][0]) = 1