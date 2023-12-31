# Важно понимать, что input возвращает строку (типы данных
# мы подробно рассмотрим во втором уроке).
# Функция float конвертирует строковое значение в вещественное,
# над которым можно выполнять арифметические операции
x = float(input('Введите первое число: '))
y = float(input('Введите второе число: '))
# Здесь мы ничего не преобразовываем, поэтому operation — строка.
operation = input('Введите знак арифметической операции: ')

# Присвоим переменной result значение None
# (None — это специальное значение, указывающее, что
# значение объекта неизвестно)
result = None
# if-elif-else (если - иначе если - иначе) — условный оператор.
# Он позволяет выполнять разные участки кода в зависимости от определённых
# условий и будет рассмотрен в уроке №3.
# Операция == проверяет два значения на равенство
if operation == '+':
    # К числам можно применять арифметические операции
    # (более подробно арифметические операции будут рассмотрены в уроке №2).
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    result = x / y
elif operation == '^':
    result = x ** y  # ** — операция возведения в степень
else:
    print('Неподдерживаемая операция')

# Так как мы во всех ветках, кроме else, присвоили result
# какое-то новое значение, а изначально оно было None,
# result останется None, если пользователь ввёл недопустимую операцию.
# Таким образом, мы выводим результат только если операция была
# допустимой и он был вычислен.
if result is not None:
    # Аргументами функции print могут быть не только строки.
    # Здесь мы выводим число.
    print(result)
