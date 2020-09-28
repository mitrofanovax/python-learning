
def array_mean(arr):
    val_mean = 0
    val_len = len(arr)

    for i in range(1,val_len):
        val_mean += arr[i]

    val_mean /= val_len-1
    arr.append(val_mean)

a = ['test',42.0, 49.0, 68.0]

array_mean(a)
print(a)
# a = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
# b = a.mean(axis=0)
# print(b)
# a = np.array(
#     [
#         #np.array([42.0, 49.0, 68.0]),
#         ['Bread', 35.0, 45.0, 90.0]
#         ['Flakes', 89.0, 100.0, 130.0],
#         ['Minced meat', 130.0, 150.0, 180.0],
#         ['Chicken breasts', 100.0, 150.0, 220.0],
#         ['Pasta', 29.0, 45.00, 60.00],
#         ['Cereals', 40.0, 59.0, 80.0],
#         ['Vegetables', 80.0, 100.0, 150.0],
#         ['Fruit', 50.0, 80.0, 150.0],
#         ['Cheeses', 80.0, 150.0, 250.0],
#         ['Sweet', 35.0, 60.0, 150.0],
#         ['Coffee', 55.0, 150.0, 239.0],
#         ['Condiments', 19.0, 30.0, 50.0],
#         ['Oil', 90.0, 150.0, 250.0],
#         {'Tea', 60.0, 80.0, 150.0}
#     ])
# a = np.array(['test',42.0, 49.0, 68.0])
# b = a.mean(axis=0)
# print(b)
#
# np.std(a, axis = 0)
#
# print('   Product name  |  Cost 1, rub |  Cost 2, rub |  Cost 3, rub')
# print('-------------------------------------------------------------')
# for row in a:
# #     print(row[0], ' | ', row[1], ' | ', row[2], ' | ', row[3])
#      print('{: <16} | {: >12.2f} | {: >12.2f} | {: >12.2f}'.format(row[0], row[1], row[2], row[3]))