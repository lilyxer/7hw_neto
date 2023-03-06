import os

# собираем текстовые файлы котрые начинаются с цифры
list_file = [elem for elem in os.listdir(path='files') if elem.endswith('txt') and elem[0].isdigit()]

my_dict_len = {}
my_dict_text = {}

for stroke in list_file:
    file_slash = os.path.join('files', stroke)
    with open(file_slash, 'r', encoding='utf-8') as file_in:
        read_file = file_in.read().splitlines()
        my_dict_len[str(stroke)] = len(read_file)
        my_dict_text[str(stroke)] = '\n'.join(read_file)
    
my_dict_len = {key: value for key, value in sorted(my_dict_len.items(), key=lambda x: x[1])}

with open('file_out.txt', 'w', encoding='utf-8') as file_out:
    for stroke in my_dict_len:
        print(f'Имя файла: {stroke}', file=file_out)
        print(f'Количество строк: {my_dict_len[stroke]}', file=file_out)
        print(my_dict_text[stroke], file=file_out)
        print(file=file_out) # простите за форматирование, но так читабельнее