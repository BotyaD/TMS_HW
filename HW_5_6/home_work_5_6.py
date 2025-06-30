import random
import time

#Задача 1
# num1 = int(input("Ввидите 1 число: "))
# num2 = int(input("Ввидите 2 число: "))
# num3 = int(input("Ввидите 3 число: "))
# print(num1 + num2 + num3)
import time

#Задача 2

# a = int(input("Введите числло: "))
# print("Следующее за числом", a, "число:", a + 1)
# print("Для числа", a, "Предыдущее число:", a - 1)

#Задача 3

# len_sm = int(input("Число в сантиметрах: ")) // 100
# print("Полное чило метров =", len_sm)

#Задача 4

# a = int(input("Введите минуты:"))
# print(a, "минут - это", a // 60, "час", a % 60, "минут")


#Задача 5

# a = int(input("Число:"))
# b = a // 100
# c = a % 100 // 10
# d = a % 10
# print("Сумма цифр =", b + c + d)
# print("Произведение цифр =", b * c * d)

#Задача 6

# a = int(input("Введите число: "))
# if a % 2 == 0:
#     print("четное")
# else:
#     print("нечетное")

#Задача 8

# listt = [1, 2, 4, 34, 434]
# listt.append("ggggg")
# print(listt)
# listt.insert(2, 1111111)
# print(listt)
# listt.append([123, "bbb", 1333])
# print(listt)
# listt.insert(1,('123', '123', 123))
# print(listt[3])
# listt.remove(2)
# print(listt)

#Задача 9

# users = {
#     "name": "Ale",
#     "phone": "123213312",
#     "email": "sdsad@g,@gmail.com"
# }
#
# users["adress"] = 11
# print(users)
#
# users[("country", "language")] = ["Germany", "ger"]
# print(users)
#
# print(users[("country", "language")])
#
# del users["name"]
# prin












# Задание 1
# Через цикл вывести в консоль все элементы списка.

list1 = ['apple', 'banana', 'cherry']

# for i in list1:
#     print(i)


# **********************************
# Используя цикл, вывести в консоль все элементы списка в обратном порядке.

# for i in list1[::-1]:
#     print(i)

# 2 вариант
# for i in reversed(list1):
#     print(i)

# 3 вариант
for i in range(len(list1)-1, -1, -1):
    print(list1[i])

#*************************************
# Используя цикл, вывести в консоль все элементы списка, а их буквы в обратном порядке.

# new_list = []
# for i in list1:
#     new_list.append(i[::-1])
# print(new_list)

# 2 вариант решения
# for i in list1:
#     reversed_ = i[::-1]
#     print(reversed_)






# Задание 2
dict1 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# Используя цикл, вывести в консоль все ключи словаря.

# for key in dict1:
#     print(key)

# Используя цикл, вывести в консоль все ключи и значения словаря.

# for key, values in dict1.items():
#     print("Ключ: ", key, ": Значение:", values)
print()
# Задание 3
# На вход пользователь вводит целое число (использовать функцию input).

# int_num = int(input("Введите целое число: "))

# Используя цикл, вывести в консоль все числа от 1 до введенного числа включительно.

# count = 1
# while count <= int_num:
#     print(count)
#     count += 1

# Используя цикл, вывести в консоль все числа от введенного числа до 1 включительно.
# count = 1
# while int_num >= count:
#     print(int_num)
#     int_num -= 1

# Используя цикл, вывести в консоль все числа от 1 до введенного числа
# включительно, которые делятся на 3 без остатка.

# for i in range(1, int_num):
#     if i % 3 == 0:
#         print(i)



# Задание 4
# На вход пользователь вводит предложение (использовать функцию input).

# str_input = input("Напишите предложение: ")

# Посчитайте количество слов в предложении и выведите результат в консоль.

# print(len(str_input))

# Используя цикл, выведите в консоль все слова предложения в обратном порядке.

# for i in reversed(str_input):
#     print(i, end= "")

# Используя цикл, создайте словарь, где ключами являются длина слов,
#           а значениями - список слов в предложении с такой длиной.
#
# str_split = str_input.split()
# new_dict = {}
# for i in str_split:
#     len_dict = len(i)
#     if len_dict not in new_dict:
#         new_dict[len_dict] = []
#     new_dict[len_dict].append(i)
# print(new_dict)

a = 0
# Задание 5
# На вход пользователь должен ввести username, email, имя и фамилию
# по очереди (использовать функцию input).
# Для каждого параметра: если введенные данные не соответствуют требованиям
# (например, username должен быть длиной от 3 до 20 символов),
# выведите сообщение об ошибке и попросите ввести данные заново.
# Создайте словарь с данными пользователя и выведите его в консоль.


# userdata = {}
#
# while True:
#     username = (input("Напишите username: "))
#     if 3 <= len(username) <= 20:
#         userdata['username'] = username
#         break
#     else:
#         print("Ошибка: username должен быть длиной от 3 до 20 символов.")
#
# while True:
#     email = str(input("Напишите email: "))
#     if 3 <= len(email) <= 20:
#         userdata['email'] = email
#         break
#     else:
#         print("Ошибка: email должен быть длиной от 3 до 20 символов.")
#
# userdata['name'] = input("Введите имя: ")
# userdata['surname'] = input("Введите фамилию: ")
#
# print("Данные пользователя: ", userdata)



# Задание 6*
# Напишите в коде случайное число от 1 до 100.
# Пользователь должен угадать это число.
# Используя цикл, попросите пользователя ввести число до тех пор, пока он не угадает.
# Если пользователь ввел не число, выведите сообщение "Вы ввели не число".
# Если пользователь ввел число, которое не попало в д
# иапазон от 1 до 100, выведите сообщение "Число не входит в диапазон от 1 до 100".
# Если пользователь ввел число больше загаданного, выведите соо
# бщение "Загаданное число меньше".
# Если пользователь ввел число меньше загаданного, выве
# дите сообщение "Загаданное число больше".
# Если пользователь угадал число, выведите сообщение "Вы угадали!" и завершите программу.

# print("Добро пожаловать в игру, Угадай число")
# rand_numb = random.randint(1,100)
# while True:
#     input_num = input("Введите число от 1 до 100 пока не угадаете: ")
#
#     if input_num.isdigit():
#         input_num = int(input_num)
#         if 1 <= input_num <= 100:
#             if input_num == rand_numb:
#                 print("Вы угадали")
#                 break
#             elif input_num > rand_numb:
#                 print("Загаданное число меньше")
#             else:
#                 print("Загаданное число больше")
#         else:
#             print("Число не входит в диапазон от 1 до 100")
#     else:
#         print("Вы ввели не число")




# Задание 7*
# Имеется структура данных пользователя.

# Используя цикл, выведите все активности по логам пользователя в консоль
# со временем и описанием.
# Если пользователь активен, выведите сообщение "Пользователь активен",
# иначе выведите "Пользователь не активен".
# Если у пользователя есть аватар, то выведите его в консоль, если нет,
# то выведите "Нет аватара".


# user1 = {
#     "userId": 2,
#     "username": "janedoe",
#     "email": "janedoe@example.com",
#     "profile": {
#         "firstName": "Jane",
#         "lastName": "Doe",
#         "birthDate": "1992-04-12",
#         "gender": "female",
#         "avatarUrl": "https://example.com/avatars/janedoe.jpg",
#         "bio": "Digital marketer and blogger."
#     },
#     "accountStatus": {
#         "isActive": True,
#         "lastLogin": "2025-01-10T09:15:00Z",
#         "createdAt": "2023-03-20T11:00:00Z"
#     },
#     "activityLogs": [
#         {
#             "timestamp": "2025-01-09T18:30:00Z",
#             "activity": "Commented on a post"
#         },
#         {
#             "timestamp": "2025-01-08T16:45:00Z",
#             "activity": "Liked a post"
#         }
#     ]
# }

# for logi in user1["activityLogs"]:
#     print(logi["timestamp"], ":", logi["activity"] )
#
# if user1["accountStatus"]["isActive"] == True:
#     print("Пользователь активен!")
# else:
#     print("Пользователь не активен")
#
# if "avatarUrl" in user1["profile"] and user1["profile"]["avatarUrl"]:
#     print("Аватар:", user1["profile"]["avatarUrl"])
# else:
#     print("Нет аватара")




# Задание 8*

# Имеется структура данных продукта.

product1 = {
    "productId": 1001,
    "productName": "Wireless Headphones",
    "description": "Noise-cancelling wireless headphones with Bluetooth 5.0 and 20-hour battery life.",
    "brand": "SoundPro",
    "category": "Electronics",
    "price": 199.99,
    "currency": "USD",
    "stock": {
        "available": True,
        "quantity": 0
    },
    "images": [
        "https://example.com/products/1001/main.jpg",
        "https://example.com/products/1001/side.jpg"
    ],
    "variants": [
        {
            "variantId": "1001_01",
            "color": "Black",
            "price": 199.99,
            "stockQuantity": 20
        },
        {
            "variantId": "1001_02",
            "color": "White",
            "price": 198.99,
            "stockQuantity": 30
        }
    ],
    "dimensions": {
        "weight": "0.5kg",
        "width": "18cm",
        "height": "20cm",
        "depth": "8cm"
    },
    "ratings": {
        "averageRating": 4.7,
        "numberOfReviews": 2
    },
    "reviews": [
        {
            "reviewId": 501,
            "userId": 101,
            "username": "techguy123",
            "rating": 5,
            "comment": "Amazing sound quality and battery life!"
        },

        {
            "reviewId": 502,
            "userId": 102,
            "username": "jane_doe",
            "rating": 4,
            "comment": "Great headphones but a bit pricey."
        }
    ]
}


# Сейчас кол-во товара на складе равно 0. Посчитайте кол-во исходя из вариантов тов
# ара на складе.
# sum_quantity = 0
#
# for top in product1["variants"]:
#    sum_quantity += top["stockQuantity"]
#
# product1["stock"]["quantity"] = sum_quantity
#
# print("Сейчас кол-во товара на складе равно:",product1["stock"]["quantity"])

# Выведите через цикл все варианты товара на складе в виде строки в формате:
# "Название - цена (кол-во на складе)".

# for variant in product1["variants"]:
#     price = variant["price"]
#     quantity = variant["stockQuantity"]
#     name = f"{product1['productName']} ({variant['color']})"
#     print(f"{name} - {price} ({quantity} на складе)")


# Используя цикл, найдите вариант товара с максимальной ценой и выведите
# его название и цену в консоль.

# max_price = 0
# max_variant = None
#
#
# for variant in product1["variants"]:
#     if variant["price"] > max_price:
#         max_price = variant["price"]
#         max_variant = variant
#
# if max_variant:
#     print(product1['productName'], max_variant['color'], '-', max_price)

# Инициализация переменных для хранения максимальной цены и соответствующего варианта




# Выведите через цикл все отзывы о товаре в виде строки в формате:
# "Пользователь - Оценка - Комментарий".

# for rev in product1["reviews"]:
#     revies = f"Пользователь: {rev['username']: <15}| Оценка: {rev['rating']: ^5} | Комментарий: {rev['comment']}"
#     print(revies)
# Посчитайте через цикл количество отзывов с оценкой 5 и выведите их количество в консоль.
# coun = 0
# for rev in product1["reviews"]:
#     if rev["rating"] == 5:
#         coun += 1
# # print(f"Кличество отзывов с оценкой 5:   {coun}")
#
# # Через цикл выведите только названия файлов картинок
# # (например, "main.jpg" и "side.jpg") товара в консоль.
#
# for photo in product1["images"]:
#     print(photo)
#
# # Используя цикл, найдите и выведите в консоль все отзывы
# # пользователя с именем "techguy123"...
#
#
# for comm in product1["reviews"]:
#     if comm["username"] == "techguy123":
#         print(f"Комменты пользователя techguy123 ")
#         print("--" * 30)
#         print(comm["comment"])










# Задание 1.
# Напишите функцию, которая принимает на вход строку (предложение),
# а возвращает самое длинное слово из строки.
def longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word('asdasdadadadasd as a as'))


# Задание 2.
# Напишите функцию, которая принимает на вход строку и заменяет в ней
# все множественные пробелы на одинарные.
#       Например: 'Hello,    world' -> 'Hello, world'

def replace_multiple_spaces(text):
    return ' '.join(text.split())



# Задание 3.
# Напишите функцию, которая принимает на вход строку и возвращает словарь,
# где ключи - это символы, а значения - количество этих символов в строке.
#       Например: 'Hello, world!' -> {'H': 1, 'e': 1, 'l': 3, 'o': 2,
#       ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}
#       Подсказка: используйте метод строки `count("a")`,
#       который возвращает количество вхождений символа в строку.

# def count_characters(text):
#     count = {}
#     for i in text:
#         if i not in count:
#             count[i] = text.count(i)
#     return count
#
# print(count_characters("asdasd asda asd kl"))
















