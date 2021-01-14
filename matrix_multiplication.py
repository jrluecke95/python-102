list1 = [[2, -2], [5, 3]]
list2 = [[-1, 4], [7, -6]]

#should equal [[-16, 20], [16, 2]]
new_list = [[0, 0], [0, 0]]
new_list[0][0] = list1[0][0]*list2[0][0] + list1[0][1]*list2[1][0]
new_list[0][1] = list1[0][0]*list2[0][1] + list1[0][1]*list2[1][1]
new_list[1][0] = list1[1][0]*list2[0][0] + list1[1][1]*list2[1][0]
new_list[1][1] = list1[1][0]*list2[0][1] + list1[1][1]*list2[1][1]

print(new_list)







# for i in range(len(list1)):
#     for j in range(len(list1[0])):
#         new_list[i][j] = list1[i][j] + list2[i][j]


#print(list1[0][0]) = 1