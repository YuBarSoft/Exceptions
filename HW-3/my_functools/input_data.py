from my_functools.myexceptions import *


class SaveToFile:
    def __init__(self):
        print('''
Необходимо ввести данные о себе в таком формате:
\tФамилия (одно слово)
\tИмя (одно слово)
\tОтчество (одно слово)
\tДата рождения (в формате dd.mm.yyyy)
\tНомер телефона (только 11 цифр)
\tПол (если мужской - m, женский - f)''')

        self.data_user = input('''Образец: Иванов Иван Иванович 01.01.1999 84951239999 m
Введите свои данные в строку ниже:\n''')

        # self.data_user = 'Петросян Иван Иванович 13.02.2050 89000567890 v'
        print(f'Вы ввели: {self.data_user}')

        self.data_arr = self.data_user.split()  # распарсиваем введенные данные
        if not self.check_len(self.data_arr):  # проверка общая на количество введенных элементов
            raise LenException(len(self.data_arr))

        self.surname = self.data_arr[0]
        self.name = self.data_arr[1]
        self.patronymic = self.data_arr[2]
        if not self.surname.isalpha():
            raise OnlyAlpha(self.surname)
        if not self.name.isalpha():
            raise OnlyAlpha(self.name)
        if not self.patronymic.isalpha():
            raise OnlyAlpha(self.patronymic)

        self.birthdate = self.data_arr[3]
        self.is_valid_date()  # проверка даты рождения

        self.phone = self.data_arr[4]
        self.is_valid_phone()  # проверка номера телефона

        self.gender = self.data_arr[5]
        self.is_valid_gender()  # проверка номера телефона

        self.create_file()

    @staticmethod
    def check_len(text):
        if len(text) != 6:
            return False
        return True

    def create_file(self):
        try:
            with open(f'{self.surname}.txt', 'a', encoding='utf-8') as f:
                f.write(f'<{self.surname}>')
                print(f'Данные записаны в файл {self.surname}.txt')
        except:
            raise SaveToFileException(f"{self.surname}.txt")

    def is_valid_date(self):
        birthdate2 = self.birthdate.split('.')
        day = int(birthdate2[0])
        month = int(birthdate2[1])
        year = int(birthdate2[2])
        # print(day, month, year)

        try:
            day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                day_count_for_month[2] = 29
            if month < 1 or month > 12:
                raise ValueError("Invalid month! Month should be between 1 and 12")
            if day < 1 or day > day_count_for_month[month]:
                raise ValueError("Invalid day! Day doesn't exist for the given month and year")
            return True
        except ValueError as e:
            raise ValidBirthDay(day, month, year)

    def is_valid_phone(self):
        if len(self.phone) != 11 or not self.phone.isdigit():
            raise PhoneNumException(self.phone)

    def is_valid_gender(self):
        if self.gender != 'm':
            raise GenderException(self.gender)
