boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(girls) != len(boys):
    print('Количество девушек и парней не равно. Кто-то может остаться беp пары.')
else:
    print(f"{' Идеальные пары: '.center(44, '=')}\n")
    print('\n'.join(f'{boy} и {girl}' for boy, girl in list(zip(sorted(boys), sorted(girls)))))

cook_book = [
    ['салат',
     [
         ['картофель', 100, 'гр.'],
         ['морковь', 50, 'гр.'],
         ['огурцы', 50, 'гр.'],
         ['горошек', 30, 'гр.'],
         ['майонез', 70, 'мл.'],
     ]
     ],
    ['пицца',
     [
         ['сыр', 50, 'гр.'],
         ['томаты', 50, 'гр.'],
         ['тесто', 100, 'гр.'],
         ['бекон', 30, 'гр.'],
         ['колбаса', 30, 'гр.'],
         ['грибы', 20, 'гр.'],
     ],
     ],
    ['фруктовый десерт',
     [
         ['хурма', 60, 'гр.'],
         ['киви', 60, 'гр.'],
         ['творог', 60, 'гр.'],
         ['сахар', 10, 'гр.'],
         ['мед', 50, 'мл.'],
     ]
     ]
]
person = 5

print(f"\n{' Список покупок: '.center(44, '=')}")
for name, dish in cook_book:
    print(f'\n{name.capitalize()}:\n' + '\n'.join(f'{ingredient}, {weight * person} {unit}' for ingredient, weight, unit in dish))
    