square_length = float(input('Введите длину стороны квадрата: '))
print(f'Периметр: {square_length * 4}')
print(f'Площадь: {square_length ** 2}')
rectangle_length = float(input('Введите длину прямоугольника: '))
rectangle_height = float(input('Введите высоту прямоугольника: '))
print(f'Периметр прямоугольника: {(rectangle_length + rectangle_height) * 2}')
print(f'Площадь прямоугольника: {rectangle_length * rectangle_height}')

print(input() * int(square_length * 4 + rectangle_length * rectangle_height))

month_salary = float(input('Введите заработную плату в месяц: '))
mortgage_percent = float(input('Введите, какой процент уходит на ипотеку: ')) / 100
life_spendings_percent = float(input('Введите, какой процент уходит на жизнь: ')) / 100
month_savings = month_salary * (mortgage_percent + life_spendings_percent)
print(f'На ипотеку было потрачено: {month_salary * mortgage_percent}')
print(f'Было накоплено: {month_savings * 12}')
