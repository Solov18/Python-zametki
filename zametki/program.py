
def show_menu(): # показать меню
    print("\nВыберите нужное действие: \n"
          "1.Отобразить все заметки\n"  
          "2.Найти заметку по номеру\n"   
          "3.Найти заметку по дате\n"    
          "4.Добавить заметку\n"          
          "5.Удалить заметку\n"          
          "6.Сохранить Заметку в текстовом формате\n" 
          "7.Закончить работу\n"
          "8.Редактировать заметку\n")
    choice = int(input())
    return choice

def read_csv(filename:str): # Читать файл csv
    data = []
    fields = ["Номер", "Заголовок", "Дата", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def write_txt(filename:str, data:list): # записать в тхт
    with open(filename, 'w', encoding='utf-8') as f_out:
        for i in range(len(data)):
            s = ''
            for value in data[i].values():
                s += value + ','
            f_out.write(f'{s[:-1]}\n')

def print_result(data:list):
    print('-'*10)
    for elem in data:
        for key in elem:
            print(f"{key} : {elem[key]}")
        print('-'*10)

def get_search_name(): #получить имя для поиска
    return input('Номер Заметки: ')

def find_by_name(data:list, name: str): #найти по названию
    result = []
    for elem in data:
        if elem['Номер'] == name:
            result.append(elem)
    return result

def find_by_number(data:list, number: str): #Найти по номеру
    result = []
    for elem in data:
        if elem['Дата'] == number:
            result.append(elem)
    return result

def get_new_user(): #получить нового пользователя
    fields = ["Номер", "Заголовок", "Дата", "Описание"]
    record = dict(zip(fields, input('Введите номер, Заголовок, дату в формате ДД.ММ.ГГ, описание\n').strip().split(',')))
    return record
    
def add_user(data:list, user:dict): # добавить пользователя
    return data.append(user)

def write_csv(filename:str, data:list): # записать в csv
    with open(filename, 'w', encoding='utf-8') as f_out:
        for i in range(len(data)):
            s = ''
            for value in data[i].values():
                s += value + ','
            f_out.write(f'{s[:-1]}\n')

def delete_by_name(data:list, name: str): #  удалить по имени 
    for elem in data:
        if elem['Номер'] == name:
            data.remove(elem)
    return data


def edit_by_name(data:list, name: str): #  удалить по имени
    for elem in data:
        if elem['Номер'] == name:
            data.remove(elem)
    return data


def work_with_phonebook(): # работа с заметками.
    choice = show_menu()
    phone_book = read_csv ('zametki\phonebook.csv')

    while(choice!=7):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            print_result(find_by_name(phone_book, name))
        elif choice == 3:
            num = input("Введите дату : ")
            print_result(find_by_number(phone_book, num))
        elif choice == 4:
            new_user = get_new_user()
            add_user(phone_book, new_user)
            write_csv('zametki\phonebook.csv', phone_book)
        elif choice == 5:
            del_name = get_search_name()
            delete_by_name(phone_book, del_name)
            write_csv('zametki\phonebook.csv', phone_book)
        elif choice == 8:
             del_name = get_search_name()
             edit_by_name(phone_book, del_name)
             write_csv('zametki\phonebook.csv', phone_book)
        elif choice == 6:
            write_txt('phon.txt.txt', phone_book) 
        choice = show_menu()
        
work_with_phonebook()