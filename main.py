# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
name = ''
age = 0
phone_number = ''
email_address = ''
additional_info = ''
mail_index = ''
mail_address = ''
# entrepreneur info
ogrnip = 0
inn = 0
checking_account = 0
name_bank = ''
bik = 0
correspondent_account = 0


def general_info_user(name_parameter, age_parameter, phone_parameter, email_parameter, add_info_parameter,
                      mail_index_parameter, mail_address_parameter):
    print(SEPARATOR)
    print('Имя:', name_parameter)
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
    print('Индекс:', mail_index_parameter)
    print('Адрес:', mail_address_parameter)
    if add_info_parameter:
        print('')
        print('Дополнительная информация:')
        print(add_info_parameter)


def count_length(length_parameter):
    count = 0
    while length_parameter > 0:
        length_parameter //= 10
        count += 1
    return count


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
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break

            elif option2 == 1:
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
                mail_index_temp = input('Введите почтовый индекс: ')
                for mit in mail_index_temp:
                    if '0' <= mit <= '9':
                        mail_index += mit
                mail_address = input('Введите почтовый адрес (без индекса): ')
                additional_info = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input entrepreneur info
                while True:
                    ogrnip = int(input("Введите ОГРНИП: "))
                    if count_length(ogrnip) == 15:
                        break
                    print("ОГРНИП должен содержать 15 цифр.")
                inn = int(input("Введите ИНН: "))
                while True:
                    checking_account = int(input('Введите расчетный счет: '))
                    if count_length(checking_account) == 20:
                        break
                    print("Расчетный счет должен содержать 20 цифр.")
                name_bank = input('Введите название банка: ')
                bik = int(input('Введите БИК: '))
                correspondent_account = int(input('Введите корреспонденский счет: '))

            else:
                print('Введите корректный пункт меню.')

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

            elif option2 == 1:
                general_info_user(name, age, phone_number, email_address, additional_info, mail_index, mail_address)

            elif option2 == 2:
                general_info_user(name, age, phone_number, email_address, additional_info, mail_index, mail_address)
                # print entrepreneur info
                print()
                print("Информация о предприниматели")
                print("ОГРНИП:", ogrnip)
                print("ИНН:", inn)
                print("Банковские реквизиты:")
                print("Р/с:", checking_account)
                print("Банк:", name_bank)
                print("БИК:", bik)
                print("К/с:", correspondent_account)

            else:
                print('Введите корректный пункт меню')

    else:
        print('Введите корректный пункт меню')
