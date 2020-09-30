
a = [
    ['Митюнистый', 650],
    ['Митяй', 847],
    ['Митюнец', 1271],
    ['Митяша', 735],
    ['Митяхер', 1505],
    ['Митяписечный', 2109],
    ['Митечка', 454],
    ['Митя', 3204],
    ['Митяшка', 150],
    ['Митрон', 935],
    ['Митюньчик', 1693],
    ['Митруша', 380]
]

customer_name_id = 0
check_id = 1

check_sum = 0
check_mean = 0

for i in a:
    #print(row[customer_name_id], row[check_id])
    check_sum += i[check_id]
    check_mean = check_sum / len(a)

print('Средний чек в ресторане:', '{:.2f}'.format(check_mean), 'руб')








