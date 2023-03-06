import pprint
import json

def parce_recipe(lst: list) -> dict:
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


file_puth = 'text.txt' # input('введите относительный либо абсолютных путь к файлу: ')

with open(file_puth, 'r', encoding='utf-8') as file:
    file_read = file.read()
    cook_book = {}
    
    for line in file_read.split('\n\n'):
        cook_book.update(parce_recipe(line))
        
pprint.pprint(cook_book)

# сериализация
# file_puth_out = '.'.join((input('введите относительный либо абсолютных путь к файлу: '), 'json'))
# with open(file_puth_out, 'w', encoding='UTF-8') as file_out:
#     json.dump(cook_book, file_out, indent=4, ensure_ascii=False) # для читаемости, занимет больше места