#Задача №49. Решение в группах
#Создать телефонный справочник с возможностью импорта и экспорта данных в
#формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
##в файле.
#1. Программа должна выводить данные
#2. Программа должна сохранять данные в текстовом файле
#3. Пользователь может ввести одну из характеристик для поиска определенной
#записи(Например имя или фамилию человека)
#4. Использование функций. Ваша программа не должна быть линейной

#tele01 = ['Иванов', 'Василий', 'Петрович',  '+79000000']
#tele01 = ';'.join(tele01)
#data = open('data01.txt', 'w', encoding = 'utf-8')
#data.writelines(tele01)
#data.close()

#tele02 = ['Пластинина', 'Елизавета', 'Николаевна',  '+79000000']
#tele02 = ';'.join(tele02)
#data = open('data02.txt', 'w', encoding = 'utf-8')
#data.writelines(tele02)
#data.close()

#tele03 = ['Абрамухина', 'Евгения', 'Владимировна',  '+79000000']
#tele03 = ';'.join(tele03)
#data = open('data03.txt', 'w', encoding = 'utf-8')
#data.writelines(tele03)
#data.close()

def find_data():
    print('Введите номер файла: ') 
    file_name = input()
    data = open(file_name+'.txt', 'r', encoding='utf-8')
    for line in data:
        print(line)
    data.close()

def new_data():
    print('Введите назание нового файла: ') 
    new_file_name = str(input())
    data = open(new_file_name+'.txt', 'w', encoding='utf-8')
    print('Введите ФИО и номер телефона (+7) через пробел: ')
    original_data = input()
    data.write(original_data)
    data.close()

def correction_data():
    print('Введите имя файла: ') 
    file_name = input()
    data = open(file_name+'.txt', 'r', encoding='utf-8')
    print(data.read())
    data.close()

    data = open(file_name+'.txt', 'w', encoding='utf-8')
    print('Введите новые ФИО и номер телефона (+7) через пробел: ')
    original_data = input()
    data.write(original_data)
    data.close()

def delete_data():
    print('Введите имя файла, который Вы хотите удалить: ')
    #data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))
    while number_file != 1 and number_file != 2:
        print('Повторите ввод')
        number_file = int(input('Введите имя файла: '))
    if number_file == 1:  
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        print(f'Удалить данную запись\n{data_first[number_journal - 1]}')
        data_first = data_first[:number_journal - 1] + data_first[number_journal + 1:]
        
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
            print('Изменения успешно сохранены!')
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        
        print(f'Удалить данную запись\n{data_second[number_journal - 1]}')
        data_second = data_second[:number_journal] + data_second[number_journal + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!') 

def change_line(dataFile, numberRow, numberFile):
    answer = input(f"Изменить данную запись\n{dataFile[numberRow]}?\n Введите ответ: ")
    while answer != 'да':
        numberRow = int(input('Введите номер записи: '))
        numberRow -= 1

    print(f"Меняем данную запись\n{dataFile[numberRow]}")
    if numberFile == 1:
        name = dataFile[numberRow].split('\n')[0]
        surname = dataFile[numberRow].split('\n')[1]
        phone = dataFile[numberRow].split('\n')[2]
        address = dataFile[numberRow].split('\n')[3]
    if numberFile == 2:
        name = dataFile[numberRow].split(';')[0]
        surname = dataFile[numberRow].split(';')[1]
        phone = dataFile[numberRow].split(';')[2]
        address = dataFile[numberRow].split(';')[3]

    answer = int(input(f"Какие данные Вы хотите поменять?\n"
                       f"1. Имя\n"
                       f"2. Фамилия\n"
                       f"3. Номер телефона\n"
                       f"4. Адрес\n"
                       f"Введите ответ: "))
    while answer < 1 or answer > 4:
        print("Вы ошиблись!\nВведите корректный номер от 1 до 4")
        answer = int(input(f"Какие данные Вы хотите поменять?\n"
                           f"1. Имя\n"
                           f"2. Фамилия\n"
                           f"3. Номер телефона\n"
                           f"4. Адрес\n"
                           f"Введите ответ: "))
    if answer == 1:
        name = name_data()
    elif answer == 2:
        surname = surname_data()
    elif answer == 3:
        phone = phone_data()
    elif answer == 4:
        address = address_data()

    if numberFile == 1:
        data_first = dataFile[:numberRow] + [f'{name}\n{surname}\n{phone}\n{address}'] + \
                     dataFile[numberRow + 1:]
        if numberRow + 1 == len(dataFile):
            data_first = dataFile[:numberRow] + [f'{name}\n{surname}\n{phone}\n{address}\n']
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
    else:
        data_second = dataFile[:numberRow] + [f'{name};{surname};{phone};{address}'] + \
                      dataFile[numberRow + 1:]
        if numberRow + 1 == len(dataFile):
            data_second = dataFile[:numberRow] + [f'{name}\n{surname}\n{phone}\n{address}\n'] + \
                         dataFile[numberRow + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!')



#from loggers import find_data, new_data, correction_data, delete_data, change_line

def interface():
    print('Здравствуйте')
    print('Вы находитесь в меню справочника')
    print('1- найти запись\n'
      '2- новая запись\n'
      '3- редактирование записи\n'
      '4- удаление записи\n'
      '5- выйти из программы\n')

    while True:
        command = int(input('Введите номер команды (1-6): '))
        if command not in [1, 2, 3, 4, 5, 6]:
            print('ошибочный запрос!')
        elif command == 1:
            find_data()
        elif command == 2:
            new_data()
        elif command == 3:
            correction_data()  
        elif command == 4:
            delete_data()  
        elif command == 5:
            change_line()
        elif command == 6:
            print('всего доброго!')
            return

if __name__ == '__main__':      
    interface()






