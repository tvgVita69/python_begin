# любой текст от символа # и до конца строки — это комментарий

# print — это функция, которая выводит информацию на экран
# параметры (аргументы) функций берутся в круглые скобки
# "Hello, World!" — это строка, которую мы выводим
#print("Hello, World!")
numbers = [5, 7, 6, 8]
#def numbers(values: list) -> float:
sum = 0

for num in numbers:
    sum += num

avg = sum / len(numbers)

print("Среднее арифметическое:", avg)