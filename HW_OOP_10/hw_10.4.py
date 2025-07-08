"""
Строки в Питоне сравниваются на основании значений символов. Т.е. если мы
захотим выяснить, что больше: Apple или Яблоко, – то Яблоко окажется
бОльшим. А все потому, что английская буква A имеет значение 65 (берется из
таблицы кодировки), а русская буква Я – 1071. Надо создать новый класс
RealString, который будет принимать строку и сравнивать по количеству
входящих в них символов. Сравнивать между собой можно как объекты класса,
так и обычные строки с экземплярами класса RealString
"""
from functools import total_ordering


@total_ordering
class RealString(str):
    def __eq__(self, other):
        if not isinstance(other, (str, RealString)):
            raise TypeError("Невозможно сравнить c числом")
        return len(self) == len(other)

    def __gt__(self, other):
        if not isinstance(other, (str, RealString)):
            raise TypeError("Невозможно сравнить c числом")
        return len(self) > len(other)



apple = RealString("Apple")
apple1 = RealString("Яблоко")
hello = "hello"

print(apple == apple1)
print(apple1 < apple)
#print(apple > 123)