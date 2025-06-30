# Напишите функцию make_sentence, которая принимает один именованный
# аргумент words, который должен быть списком строк, и возвращает строку,
# составленную из элементов списка, разделенных пробелами и
# заканчивающуюся точкой. Если аргумент words не указан, то по умолчанию
# используется список ["This", "is", "a", "sentence"].
# Пример вызова:
# make_sentence(words=["Python", "is", "fun"])
# # Python is fun.



#def make_sentence(words = None):
#     if words is None:
#         words = ["This", "is", "a", "sentence"]
#
#     return ' '.join(words) + '.'



# sentence1 = make_sentence(words=["Python", "is", "fun"])
# print(sentence1)
#sentence2 = make_sentence()
#print(sentence2)





# Напишите функцию sum_of_squares, которая принимает произвольное
# количество позиционных аргументов, которые должны быть числами, и
# возвращает сумму их квадратов. Если функции не передано ни одного
# аргумента, она должна вернуть 0

#1 Вариант
# def sum_of_squares(*args):
#     if not args:
#         return 0
#     return sum(x ** 2 for x in args)
#
#
# print(sum_of_squares(2, 2))

#2 Вариант
# def sum_of_squares(*args):
#     if not args:
#         return 0
#     return sum(map(lambda x: x ** 2, args))
#
#
# result = sum_of_squares (1, 2, 3, 4)
#
# print(result)



# Напишите функцию greet, которая принимает два именованных аргумента:
# name и language. Аргумент name должен быть строкой, а аргумент language
# # должен быть одним из трех возможных значений: "en", "ru" или "fr".
# # Функция должна возвращать приветствие на выбранном языке.
# # Если аргумент language не указан, то по умолчанию используется "en".
# # Пример вызова:
# # greet(name="Anna", language="en")
# # Hello, Anna!
#
# def greet(name, language="en"):
#
#     if not name:
#         return f"Вы не ввели имя"
#
#     if language == 'en':
#         return f"Hello {name}"
#
#     elif language == 'ru':
#         return f"Привет {name}"
#
#     elif language == 'fr':
#         return f"Bonjour {name}"
#
#     else:
#         return f"Ваш введeнный язык '{language}' не поддарживается"
#
#
# print(greet(name="Anna", language="ru"))
#




# Напишите функцию print_info, которая принимает произвольное
# количество именованных аргументов (**kwargs) и выводит их в формате
# "key: value" по одной паре на строку. Напоминаю, что kwargs в функции
# будет словарем. Если функции не передано ни одного аргумента, она должна
# вывести "No info given.".
# Пример вызова:
# print_info(name="Alex", age=25, city="Amsterdam")

# def print_info(**kwargs):
#     if not kwargs:
#         print(f"No info given.")
#     else:
#         for key, value in kwargs.items():
#             print(f"{key}: {value}")
#
#
# print_info(name="Alex", age=25, city="Amsterdam")



# Напишите функцию print_table, которая принимает произвольное
# количество именованных аргументов в виде пар ключ-значение и выводит их
# в виде таблицы с двумя столбцами: "Key" и "Value". Если функции не
# передано ни одного аргумента, она должна вывести "No data given.".
# Пример вызова:
# print_table(name="Bob", age=30, city="Amsterdam")

# def print_table(**kwargs):
#     print(f"|   Key    |   Value   |")
#     print(f"|----------|-----------|")
#     if not kwargs:
#         print("No data given")
#     else:
#         for key, value in kwargs.items():
#             print(f"| {key :<9}| {value :<9} |")
#
#
# print_table()


# Напишите функцию calculate, которая принимает произвольное количество
# позиционных аргументов, которые должны быть числами, и один
# именованный аргумент operation, который должен быть одним из четырех
# возможных значений: "+", "-", "*" или "/".
# Функция должна возвращать результат выполнения указанной операции над
# всеми числами в порядке их передачи.
# Если функции не передано ни одного позиционного аргумента, она должна
# вернуть 0.
# Если аргумент operation не указан, то по умолчанию используется "+".
# Пример вызова: calculate(1, 2, 3, operation="*")


# def calculate(*args, operation = '+'):
#     if not args:
#         return None
#     if operation == '+':
#         result = 0
#         for num in args:
#             result += num
#         return result
#     elif operation == '-':
#         result = args[0]
#         for num in args[1:]:
#             result -= num
#         return result
#     elif operation == '*':
#         result = 1
#         for num in args:
#             result *= num
#         return result
#     elif operation == '/':
#         result = args[0]
#         for num in args[1:]:
#             result /= num
#         return result
#     else:
#         raise ValueError(f"Ошибка значения {operation}.Должно быть '+', '-', '*', '/'")
#
#
#
# print(calculate(1, 2, 3, operation="*"))
# print(calculate(1, 2, 3, operation="-"))
# print(calculate(1, 2, 3, operation="+"))
# print(calculate(1, 2, 3, operation="/"))
# print(calculate())




# Напишите функцию print_triangle, которая принимает один именованный
# аргумент height, который должен быть положительным целым числом, и
# выводит равнобедренный треугольник из символов "*" с заданной высотой.
# Если аргумент height не указан, то по умолчанию используется число 5.
# Пример вызова: print_triangle(height=4)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# def print_triangle(height=5):
#     if not isinstance(height, int) or height <= 0:
#         raise ValueError("высота должна быть положительным целым числом")
#
#     for i in range(1, height + 1):
#         spaces = " " * (height - i)
#         stars = "*" * (2 * i - 1)
#         print(spaces + stars)
#
# print_triangle(height=10)





# Напишите функцию create_post, которая создает пост для блога,
# основываясь на переданных параметрах. Обязательными параметрами
# являются: заголовок, содержимое и автор. Необязательным параметром
# является категория. Если она не была передана, то по умолчанию будет
# текущая значение “general”. Функция должна возвращать словарь поста

#
# def create_post(title, content, author, category = "General"):
#
#     post={
#         "title": title,
#         "content": content,
#         "author": author,
#         "category": category
#     }
#
#     return post
#
#
# print(create_post (title = "Как быстро научиться программировать",
#             content = "нужно решать много задач",
#             author = "John"))




# Напишите функцию create_product, которая создает товар для
# интернетмагазина, основываясь на переданных параметрах. Обязательными
# параметрами являются: имя, цена и категория. Необязательным параметром
# является рейтинг. Если он не был передан параметр, то по умолчанию будет
# 0. Функция должна возвращать словарь товара


# def create_product(name, price, cetegory, reyt = 0):
#     products = {
#         "name": name,
#         "price": price,
#         "category": cetegory,
#         "reyt": reyt
#     }
#     return products
#
#
# print(create_product("banan","20", "fructs", 4))



# Напишите функцию create_student, которая создает словарь студента
# для учебного заведения, основываясь на переданных параметрах.
# Обязательными параметрами являются: имя, фамилия, отчество и группа.
# Также дополнительными параметрами могут быть: дата поступления в виде
# строки «19.10.2023», средний бал, семестр обучения, номер телефона, адрес.
# Функция должна возвращать словарь студента только с переданными
# данными, если некоторые данные не были переданы, то их не должно быть
# в словаре.

# def create_student(name, surname, lastname, group, **kwargs):
#     data_students = {
#         "name": name,
#         "surname": surname,
#         "lastname": lastname,
#         "group": group,
#     }
#     data_students.update(kwargs)
#     return data_students
#
#
# print(create_student("Владимир", "Иванов", "Эдуардович",
#                      "123", address = "Якубова 30"))


