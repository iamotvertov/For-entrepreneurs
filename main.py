# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
name = ''
age = 0
phone_number = ''
email_address = ''
additional_info = ''


def general_info_user(name_parameter, age_parameter, phone_parameter, email_parameter, add_info_parameter):
    print(SEPARATOR)
    print('Имя:    ', name_parameter)
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', phone_parameter)
    print('E-mail: ', email_parameter)
    if add_info_parameter:
        print('')
        print('Дополнительная информация:')
        print(add_info_parameter)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                name = input('Введите имя: ')
                while 1:
                    # validate user age
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    print('Возраст должен быть положительным')

                inter_standard_number = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone_number = ''
                for isn in inter_standard_number:
                    if isn == '+' or ('0' <= isn <= '9'):
                        phone_number += isn

                email_address = input('Введите адрес электронной почты: ')
                additional_info = input('Введите дополнительную информацию:\n')
            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(name, age, phone_number, email_address, additional_info)

            elif option2 == 2:
                general_info_user(name, age, phone_number, email_address, additional_info)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')
