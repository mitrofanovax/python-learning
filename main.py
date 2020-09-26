distance = 1.500
years = 1
days_training = 200
times_year = years * days_training
sum_distance = 0
kkal_ksu = 0
kkal_mity = 0
kkal_km = [50, 110]

for i in range(times_year):
    sum_distance += distance

kkal_ksu  = kkal_km[0] * sum_distance
kkal_mity = kkal_km[1] * sum_distance

print('Количество тренировок:', times_year, 'шт')
print('Ваш путь составил: {:.0f}'.format(sum_distance), 'км')
print('Всего потрачено ккалорий - Ксюша:', kkal_ksu)
print('Всего потрачено ккалорий - Митя:', kkal_mity)
