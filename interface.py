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

from loggers import find_data, new_data, correction_data, delete_data, change_line

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
        
interface()





