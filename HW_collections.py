from pprint import pprint 
#################### Задание 1 ######################
print(f'{" Задание 1 ".center(44, "=")}\n')

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
i = 0
while i < len(geo_logs):
  if 'Россия' not in list(geo_logs[i].values())[0]:
    del geo_logs[i]
  else:
    i += 1
pprint(geo_logs)

#################### Задание 2 ######################
print(f'\n{" Задание 2 ".center(44, "=")}\n')

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
arr = []
for item in ids:
  arr.extend(ids[item])
print(list(set(arr)))

#################### Задание 3 ######################
print(f'\n{" Задание 3 ".center(44, "=")}\n')

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]
arr = [len(elem.split()) for elem in queries]
dict_ = {}
for elem in arr:
  if elem not in dict_:
    dict_[elem] = arr.count(elem) / (len(arr) / 100)
  else:
    continue
print('Распределение количества слов в запросе в процентах(%):\n')
for key in dict_:
  print(f'При количестве слов в запросе: {key} = {dict_[key]:.2f}%')


#################### Задание 4 ######################
print(f'\n{" Задание 4 ".center(44, "=")}\n')

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
max_amount = 0
company_name = None
for key, value in stats.items():
  if max_amount > value:
    continue
  else:
    max_amount = value
    company_name = key
print(company_name)
  
#################### Задание 5 ######################
print(f'\n{" Задание 5 ".center(44, "=")}\n')

arr = ['2018-01-01', 'yandex', 'cpc', 100]

# решение через цикл

while len(arr) > 1:
  x = {arr.pop(-2): arr.pop()}
  arr.append(x)
print(arr.pop())

# решение с помощью функции с рекурсией
arr2 = ['2018-01-01', 'yandex', 'cpc', 100]
def func(arr):
  if len(arr) == 1:
    print(arr.pop())
  else:
    x = {arr.pop(-2): arr.pop()}
    arr.append(x)
    func(arr)
func(arr2)

