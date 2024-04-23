
import datetime as d

# try:
#     a = int(input('Введите число:'))
#     print(f'Ваше число: {a}')
# except ValueError:
#     print(f'Вы ввели не число!')

a = d.datetime.utcnow()
print(f'UTC время : {a}')
b = d.datetime.now()
print(f'Время моего часового пояса : {b}')
g = b - a
print(f'Разность времени : {g}')

c = d.datetime.now() - d.timedelta(hours=1)
print(f'UTC минус один час : {c}')

print(d.date.today())
print(d.date(year=2024, month=4, day=24))