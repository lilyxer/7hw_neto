import pprint
import json

def parce_recipe(lst: list) -> dict:
    """Разбор строк на словарь"""
    my_d = {}
    titles = ['ingredient_name', 'quantity', 'measure']
    recipe = iter(lst.splitlines())
    recipe_title = next(recipe)
    len_line = int(next(recipe))
    while len_line:
        stroke = next(recipe).split(' | ')
        my_d.setdefault(recipe_title, []).append(dict(zip(titles, stroke)))
        len_line -= 1
    return my_d

def get_shop_list_by_dishes(lst: list, quan: int) -> dict|str:
    """используя названия блюд из нашего списка собираем ингридиенты из рецептов"""
    dict_ingredients = {}
    if quan:
        for elem in lst: # перебираем названия блюд
            for ingredients in cook_book[elem]: # заходим в словарь блюда
                name = ingredients['ingredient_name']
                measure = ingredients['measure']
                quantity = ingredients['quantity']
                dict_ingredients.setdefault(name, {}).setdefault('measure', measure)
                dict_ingredients[name]['quantity'] = dict_ingredients.setdefault(name, {}).setdefault('quantity', 0) + int(quantity) * quan
        return dict_ingredients
    return 'гостей не будет, ужин отменяется'


file_puth = 'files\\text.txt' # input('введите относительный либо абсолютных путь к файлу: ')

with open(file_puth, 'r', encoding='utf-8') as file:
    file_read = file.read()
    cook_book = {}
    
    for line in file_read.split('\n\n'):
        cook_book.update(parce_recipe(line))

print('Наша поваренная книга')
pprint.pprint(cook_book)
     
print('Выберите что мы будем готовить и на сколько персон\nУмеем готовить:')
print(*cook_book, sep=', ')
list_cook = ['Запеченный картофель', 'Омлет'] # [] для интерактивности можно свой список собрать
# answer = input('Добавьте блюдо... ')
# while answer in cook_book:
#     list_cook.append(answer)
#     answer = input('Что нибудь ещё? ')
# else:
#     print('Рецепта на это блюдо у нас нет')

print('\nДля ужина нам понадобится...\n')
pprint.pprint(get_shop_list_by_dishes(list_cook, int(input('Сколько персон? '))))

# сериализация
# file_puth_out = '.'.join((input('введите относительный либо абсолютных путь к файлу: '), 'json'))
# with open(file_puth_out, 'w', encoding='UTF-8') as file_out:
#     json.dump(cook_book, file_out, indent=4, ensure_ascii=False) # для читаемости, занимет больше места