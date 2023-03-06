# netology
<h3>Задача №1</h3>
<div>
    <ul>
    <li>В одном файле может быть произвольное количество блюд.</li>
    <li>Читать список рецептов из этого файла.</li>
    <li>Соблюдайте кодстайл, разбивайте новую логику на функции и не используйте глобальных переменных.</li>
    </ul>
    <p>Должен получится следующий словарь</p>
    <code>cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }</code></div>
<h3>Задача №2</h3>
<div>
    <p>Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить</p>
    <p><i>get_shop_list_by_dishes(dishes, person_count)</i></p>
    <p>На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для такого вызова</p>
    <p><i>get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)</i></p>
    <p>Должен быть следующий результат:</p>
<code>{
  'Картофель': {'measure': 'кг', 'quantity': 2},
  'Молоко': {'measure': 'мл', 'quantity': 200},
  'Помидор': {'measure': 'шт', 'quantity': 4},
  'Сыр гауда': {'measure': 'г', 'quantity': 200},
  'Яйцо': {'measure': 'шт', 'quantity': 4},
  'Чеснок': {'measure': 'зубч', 'quantity': 6}
}</code>
<p>>Обратите внимание, что ингредиенты могут повторяться</p></div>
