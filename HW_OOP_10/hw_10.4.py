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
class RealString:
    def __init__(self, string):
        self.string = str(string)

    def __len__(self):
        return len(self.string)

    def __eq__(self, other):
        if isinstance(other, RealString):
            return len(self.string) == len(other.string)
        if isinstance(other, str):
            return len(self.string) == len(other)
        raise TypeError(f"Невозможно сравнить ")

    def __lt__(self, other):
        if isinstance(other, RealString):
            return len(self.string) < len(other.string)
        if isinstance(other, str):
            return len(self.string) < len(other)
        raise TypeError(f"Невозможно сравнить ")


ru = RealString("Яблоко")
en = RealString("Apple")

print(en < ru)
print(en <= ru)
print(ru <= en)
#print(ru == 123456)