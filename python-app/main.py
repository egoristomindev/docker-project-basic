import calendar

print('Добро пожаловать в суперкалендарь\n')

year = int(input('Пожалуйста введите год: '))
month = int(input('Введите номер любого месяца: '))

print(calendar.month(year, month))
print('Всего хорошего')
