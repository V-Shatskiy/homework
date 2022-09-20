print(f'{" Калькулятор процентной ставки ".center(44, "=")}\n')

eastern_region = ['амурская область',
                  'республика бурятия',
                  'еврейская автономная область',
                  'забайкальский край',
                  'камчатский край',
                  'магаданская область',
                  'приморский край',
                  'республика саха', 'якутия',
                  'сахалинская область',
                  'хабаровский край',
                  'чукотский автономный округ']
children_count_discount = 0
salary_project_discount = 0
insurance_discount = 0
basic_mortgage_rate = float(input('Введите базовую процентную ставку: '))
region = input('Введите регион проживания: ').lower()
if region in eastern_region:
    mortgage_rate = 2.0
else:
    children_count = int(input('Ввдите количество детей: '))
    if children_count > 3:
        children_count_discount = 1.0
    salary_project = input('Есть ли зарплатный проект(да/нет): ').lower()
    if salary_project == 'да':
        salary_project_discount = 0.5
    insurance = input('Оформлено ли страхование(да/нет): ').lower()
    if insurance == 'да':
        insurance_discount = 1.5
    mortgage_rate = basic_mortgage_rate - children_count_discount - salary_project_discount - insurance_discount
print(f'Итоговая процентная ставка по ипотеке: {mortgage_rate}%')

print(f'\n{" Знак зодиака ".center(44, "=")}\n')

data = {"январь": ("Козерог", 21, "Водолей"),
        "февраль": ("Водолей", 19, "Рыбы"),
        "март": ("Рыбы", 21, "Овен"),
        "апрель": ("Овен", 21, "Телец"),
        "май": ("Телец", 22, "Близнецы"),
        "июнь": ("Близнецы", 22, "Рак"),
        "июль": ("Рак", 23, "Лев"),
        "август": ("Лев", 24, "Дева"),
        "сентябрь": ("Дева", 24, "Весы"),
        "октябрь": ("Весы", 24, "Скорпион"),
        "ноябрь": ("Скорпион", 23, "Стрелец"),
        "декабрь": ("Стрелец", 22, "Козерог")}
long_months = ['январь', 'март', 'май', 'июль', 'август', 'октябрь', 'декабрь']
month = input('Введите месяц: ').lower()
if month not in list(data.keys()):
    print('Неверно введен месяц')
else:
    if month in long_months:
        maxday = 31
    elif month == 'февраль':
        maxday = 29
    else:
        maxday = 30
    try:
      day = int(input('Введите число: '))
    except ValueError:
        print('Неверный формат ввода')
    else:
      if day > maxday or day <= 0:
          print('Неверно введено число')
      else:
          if day < data[month][1]:
              zodiac = data[month][0]
          else:
              zodiac = data[month][2]
          print(zodiac)
    