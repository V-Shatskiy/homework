import sys

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def people(doc_list=documents):
    doc_id = input('Введите номер документа: ')
    for doc in doc_list:
        if doc_id == doc['number']:
            return doc['name']            
    else:
        return 'Номер документа не найден'


def shelf_search(dir_dict=directories):
    doc_id = input('Введите номер документа: ')
    for shelf in dir_dict:
        if doc_id in dir_dict[shelf]:
            return f'Запрашиваемый документ находится на полке номер {shelf}'            
    else:
        return 'Номер документа не найден'
      

def add_doc(doc_list=documents, dir_dict=directories):
    shelf = input('Введите номер полки на которой будет храниться документ: ')
    if shelf not in dir_dict:
        return 'Указанной полки не существует'
    else:
        data = {'type': input('Введите тип документа: '),
                'number': input('Введите номер документа: '),
                'name': input('Введите имя: ')}
        doc_list.append(data)
        dir_dict[shelf].append(data['number'])
        return f'Данные успешно добавлены в список документов и на полку {shelf}'


def print_list(doc_list=documents):
    result = 'Список документов:\n'
    for doc in doc_list:
        result +=  ' | '.join(list(doc.values())) + '\n'         
    return result.rstrip('\n')


def add_shelf(dir_dict=directories):
    shelf = input('Введите номер добавляемой полки: ')
    if shelf in dir_dict:
        return 'Такая полка уже существует'
    else:
        dir_dict[shelf] = []
        return f'Полка номер {shelf} успешно добавлена'


def move(dir_dict=directories):
    target_shelf = input('Введите номер целевой полки: ')
    if target_shelf not in dir_dict:
        return 'Указанной полки не существует'
    doc_id = input('Введите номер документа: ')
    for key, value in dir_dict.items():
        if doc_id in value:
            dir_dict[key].remove(doc_id)
            dir_dict[target_shelf].append(doc_id)          
            return f'Документ под номером {doc_id} перемещен на полку {target_shelf}'          
    else:
        return 'Неверный номер документа'
    

         
def delete(doc_list=documents, dir_dict=directories):
    doc_id = input('Введите номер документа: ')
    for shelf in dir_dict:
        if doc_id in dir_dict[shelf]:
            dir_dict[shelf].remove(doc_id)
            break
    else:
        return 'Неверный номер документа'
    for data in doc_list:
        if doc_id == data['number']:
            doc_list.remove(data)
            return 'Документ удален с полки и из списка документов'            

  
def show_help():
    return ' Список команд: '.center(50, '=') + '''\np  - People - Вывести имя человека по номеру документа
s  - Shelf - Вывести номер полки на которой находится документ с соответствующим номером
l  - List - Вывести список всех документов
a  - Add - Добавить новый документ в каталог и в перечень полок
d  - Delete - Удалить полностью документ из каталога и его номер из перечня полок
m  - Move - Переместить документ с текущей полки на целевую
as - Add Shelf - Добавить новую полку в перечень полок
q  - Quit - Выход из программы'''


def main():
    command = {'h': show_help, 'p': people, 's': shelf_search, 'l': print_list, 'a': add_doc, 'd': delete, 'm': move, 'as': add_shelf, 'q': sys.exit}
    print(show_help())
    while True:
        print(f'{"=" * 50}\nh  - Help - Вывести список доступных комманд\n{"=" * 50}')
        choice = input('Введите команду: ')
        if choice not in command:
            print('Неверная комманда')
        else:
            print(command[choice]())
      

if __name__ == "__main__":
  main()
