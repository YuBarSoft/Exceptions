class LenException(Exception):
    def __init__(self, length):
        self.length = length

    def __str__(self):
        return f'''\tError Code: 1
\tВместо 6 элементов Вы ввели: {self.length}!'''


class OnlyAlpha(Exception):
    def __init__(self, abc):
        self.abc = abc

    def __str__(self):
        return f'''\tError Code: 3
\tФамилия, имя и отчество должны содержать только буквы, а Вы ввели: {self.abc}'''


class ValidBirthDay(Exception):
    def __init__(self, day, month, year):
        if 0 < day < 10:
            day = '0' + str(day)
        if 0 < month < 10:
            month = '0' + str(month)
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'''\tError Code: 5
\tТакая дата не существует: {self.day}.{self.month}.{self.year}'''


class PhoneNumException(Exception):
    def __init__(self, phone):
        self.phone = phone

    def __str__(self):
        return f'''\tError Code: 6
\tТелефонный номер должен состоять из 10 цифр. Вы ввели: {self.phone})'''


class GenderException(Exception):
    def __init__(self, gender):
        self.gender = gender

    def __str__(self):
        return f'''\tError Code: 7
\tПол может быть "f" или "m". Вы ввели: {self.gender}'''


class SaveToFileException(Exception):
    def __init__(self, file):
        self.file = file

    def __str__(self):
        return f'''\tError Code: 2
\tДанные не удалось записать в файл {self.file}!'''
