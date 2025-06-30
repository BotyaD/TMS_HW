# # Напишите код, который принимает список чисел и возвращает новый список,
# # содержащий только четные числа из исходного списка. Используйте функцию
# # filter и лямбда-выражение
#
# list_num = [1, 2, 3, 4, 5, 6, 7, 8]
# not_even = list(filter(lambda x: x % 2 == 0, list_num))
# print(not_even)
# #
# def even(n):
#     return n % 2 == 0
#
#
# list_1 = list(filter(even, list_num))
#
# # Напишите код, который принимает список кортежей вида (имя, возраст) и
# # возвращает новый список, отсортированный по возрастанию возраста.
# # Используйте функцию sorted и ключ сортировки
#
# def sorted_tuple(people):
#     return sorted(people, key=lambda x: x[1])
#
#
# people = [("Анна", 25),
#          ("Иван", 20),
#          ("Мария", 30),
#          ("Петр", 18)
#          ]
# people_sorted = sorted_tuple(people)
# print(people_sorted)
#
#
# # Напишите код, который принимает список строк и возвращает новый список,
# # содержащий только те строки, которые начинаются с гласной буквы. (Да да,
# # снова эти гласные) Используйте функцию filter и множество
#
# def str_(str_text):
#     vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
#     result = list(filter(lambda x: x[0].lower() in vowels, str_text))
#     return result
#
#
# print(str_(["Апельсин", "банан","Ифывфыв", "Игрушка", "ёжик", "Яблоко"]))
#
#
#
#
#
# # Напишите код, который принимает список чисел и возвращает новый список,
# # содержащий квадраты этих чисел. Используйте функцию map и lambda
#
# def nums(*args):
#     return list(map(lambda x: x ** 2, args))
#
# print(nums(1, 2, 3, 4))
#
#
#
# # Напишите код, который принимает список слов и возвращает новый список,
# # отсортированный по убыванию длины слов. Используйте функцию sorted и
# # обратный порядок сортировки.
#
# def soted_list(lists):
#     return sorted(lists, key=len, reverse= True)
#
#
# print(soted_list(["Апельсин", "банан","Ифывфыв", "Игрушка", "ёжик", "Яблоко"]))
# #
#
# fr = ["Апельсин", "банан","Ифывфыв", "Игрушка", "ёжик", "Яблоко"]
# fr.sort(reverse=True)
# print(fr)
#
#
#
#
#
# # Напишите код, который принимает строку и возвращает список, содержащий
# # только те буквы, которые встречаются в слове “python”. Используйте функцию
# # filter и оператор in.
#
# str_list = "Pyatahaoan"
# word = "python"
#
# result = list(filter(lambda x: x in word, str_list.lower()))
# print(result)
#
#
# # Напишите код, который принимает список чисел и возвращает новый список,
# # содержащий эти же числа, умноженные на 10. Используйте функцию.
#
#
# def int_nums(*args)->list:
#     result = []
#     for num in args:
#         result.append(num * 10)
#     return result
#
#
# result = int_nums(1, 2, 3, 4, 5, 6)
# print(result)
#
#
# # Напишите код, который принимает список слов и возвращает новый список,
# # отсортированный по алфавиту. Используйте функцию sorted
#
# def sort_words(*args)->list:
#     return sorted(args)
#
#
# print(sort_words("hello", "world", "code", "program", "algorithm",
#     "data", "science", "string", "integer", "float",
#     "loop", "break", "continue", "return", "yield"))
#
#
# # 2 вариант
# list_words = ["hello", "world", "code", "program", "algorithm",
#     "data", "science", "string", "integer", "float",
#     "loop", "break", "continue", "return", "yield"]
#
# sorted_list = sorted(list_words)
# print(sorted_list)
#
# # Напишите функцию, которая принимает список строк и возвращает новый
# # список, содержащий только те строки, которые являются палиндромами.
# # Палиндром — это слово, которое читается одинаково слева направо и справа
# # налево. Используйте функцию filter и сравнение строк
#
# def polin_funk(listt_):
#     return list(filter(lambda x: x.lower() == x.lower()[::-1], listt_))
#
#
# listt = [
#     "ТОПОТ",
#     "мадам",
#     "python",
#     "казак",
#     "программа"
# ]
#
# palin = polin_funk(listt)
# print(palin)
#
# #2 вариант
# polin_list = list(filter(lambda x: x == x[::-1], listt))
#
# print(polin_list)
#
#
# # Напишите код, который принимает список слов и возвращает новый список,
# # отсортированный по возрастанию количества гласных букв в словах.
# # Используйте функцию sorted и ключ сортировки
#



def count_vowels(srt_list):
    ru_vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
    count = 0
    for i in srt_list:
        if i in ru_vowels:
            count += 1
    return count


increasing_vowels = ["окно", "облако", "кот", "сок", "электрик"]


result = sorted(increasing_vowels, key=count_vowels)
print(result)


# # Напишите код, который принимает список чисел и возвращает новый список,
# # содержащий только четные числа из исходного списка. Используйте функцию
# # filter и лямбда-выражение
#
# list_num = [1, 2, 3, 4, 5, 6, 7, 8]
# not_even = list(filter(lambda x: x % 2 != 0, list_num))
# print(not_even)
#
# def not_even(n):
#     return n % 2 != 0
#
#
# list_1 = list(filter(not_even, list_num))
#
# # Напишите код, который принимает список кортежей вида (имя, возраст) и
# # возвращает новый список, отсортированный по возрастанию возраста.
# # Используйте функцию sorted и ключ сортировки

def sorted_tuple(people):
    return sorted(people, key=lambda x: x[1])


people = [("Анна", 25),
         ("Иван", 20),
         ("Мария", 30),
         ("Петр", 18)
         ]
people_sorted = sorted_tuple(people)
print(people_sorted)


# # Напишите код, который принимает список строк и возвращает новый список,
# # содержащий только те строки, которые начинаются с гласной буквы. (Да да,
# # снова эти гласные) Используйте функцию filter и множество

def str_(str_text):
    vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
    result = list(filter(lambda x: x[0].lower() in vowels, str_text))
    return result



print(str_(["Апельсин", "банан","Ифывфыв", "Игрушка", "ёжик", "Яблоко"]))


# # Напишите код, который принимает список чисел и возвращает новый список,
# # содержащий квадраты этих чисел. Используйте функцию map и lambda

def nums(*args):
    return list(map(lambda x: x ** 2, args))

print(nums(1, 2, 3, 4))



# # Напишите код, который принимает список слов и возвращает новый список,
# # отсортированный по убыванию длины слов. Используйте функцию sorted и
# # обратный порядок сортировки.
#
def soted_list(lists):
    return sorted(lists, reverse= True)
print(soted_list(["Апельсин", "банан","Ифывфыв", "Игрушка", "ёжик", "Яблоко"]))


fr = ["Апельсин", "банан","Ифывфыв", "Игрушка", "ёжик", "Яблоко"]
fr.sort(reverse=True)
print(fr)





# # Напишите код, который принимает строку и возвращает список, содержащий
# # только те буквы, которые встречаются в слове “python”. Используйте функцию
# # filter и оператор in.

str_list = "Pyatahaoan"
word = "python"

result = list(filter(lambda x: x in word, str_list.lower()))
print(result)


# # Напишите код, который принимает список чисел и возвращает новый список,
# # содержащий эти же числа, умноженные на 10. Используйте функцию.
#
#
def int_nums(*args)->list:
    result = []
    for num in args:
        result.append(num * 10)
    return result


result = int_nums(1, 2, 3, 4, 5, 6)
print(result)

#
# # Напишите код, который принимает список слов и возвращает новый список,
# # отсортированный по алфавиту. Используйте функцию sorted
#
def sort_words(*args)->list:
    return sorted(args)


print(sort_words("hello", "world", "code", "program", "algorithm",
    "data", "science", "string", "integer", "float",
    "loop", "break", "continue", "return", "yield"))
#
#
# 2 вариант
list_words = ["hello", "world", "code", "program", "algorithm",
    "data", "science", "string", "integer", "float",
    "loop", "break", "continue", "return", "yield"]

sorted_list = sorted(list_words)
print(sorted_list)
#
# # Напишите функцию, которая принимает список строк и возвращает новый
# # список, содержащий только те строки, которые являются палиндромами.
# # Палиндром — это слово, которое читается одинаково слева направо и справа
# # налево. Используйте функцию filter и сравнение строк

def polin_funk(listt_):
    return list(filter(lambda x: x == x[::-1], listt_ ))


listt = [
    "топот",
    "мадам",
    "python",
    "казак",
    "программа"
]
#
# palin = polin_funk(listt)
# print(palin)
#
# #2 вариант
polin_list = list(filter(lambda x: x == x[::-1], listt))

print(polin_list)

#
# # Напишите код, который принимает список слов и возвращает новый список,
# # отсортированный по возрастанию количества гласных букв в словах.
# # Используйте функцию sorted и ключ сортировки
#
def sort_in_alf(srt_list):
    ru_vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    result = sorted(srt_list, key=ru_vowels, reverse=True)
    return result
#
words_with_increasing_vowels = [
    "кот",
    "сок",
    "окно",
    "облако",
    "электрик"
]
sort_in_alf(words_with_increasing_vowels)







# Напишите код, который принимает список строк и возвращает новый список,
# содержащий эти же строки в верхнем регистре. Используйте функцию map и
# встроенный метод строк upper

words = [
    "кот",
    "сок",
    "окно",
    "облако",
    "электрик"
]
uper_new_list = list(map(lambda word: word[0].upper() + word[1::], words ))

print(uper_new_list)




# Напишите код, который принимает список строк и возвращает новый список,
# содержащий эти же строки с добавленным префиксом “Hello”. Используйте
# функцию map и конкатенацию строк
def pref(listt):
    return list(map(lambda word: "Hello " + word, listt))

words = [
    "кот",
    "сок",
    "окно",
    "облако",
    "электрик"
]

print(pref(words))


# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества букв “a” в словах. Используйте
# функцию sorted и ключ сортировки

words = [
    "электрик",
    "кот",
    "сок",
    "окно",
    "облако",
    "фывaaa",
    "папdsfa",
    "цйуsdfaA"
]


sort_str = sorted(words, key= lambda x:x.count("a"))

print(sort_str)


#
#
# #  Напишите код, который принимает список слов и возвращает новый список,
# # отсортированный по возрастанию количества уникальных букв в словах.
# # Используйте функцию sorted и ключ сортировки
#
words = [
    "электрик",
    "кот",
    "сок",
    "окно",
    "облако",
    "фывaaa",
    "папdsfa",
    "цйуsdfaA",
    "кот"
]
sorter_words = sorted(words, key=lambda word: len(set(word)))

print(sorter_words)


def wolve(str_):
    ru_vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
    count = 0
    for i in str_:
        if i in ru_vowels:
            count += 1
    return count


increasing_vowels = ["окно", "облако", "кот", "сок", "электрик"]
# sorteding = sorted(increasing_vowels, key=wolve)
# print(sorteding)
list2 = [x for x in increasing_vowels if x in 'аеёиоуыэюяАЕЁИОУЫЭЮЯ']

print(list2)