"""
Напишите класс Person, который имеет атрибуты name (имя), age (возраст)
и gender (пол). Класс должен иметь следующие методы:
• Конструктор, который принимает три параметра: name, age и gender, и
инициализирует соответствующие атрибуты.
• Метод str, который возвращает строковое представление объекта класса
Person в формате “Имя: name, Возраст: age, Пол: gender”.
• Метод get_name, который возвращает значение атрибута name.
• Метод set_name, который принимает один параметр: new_name, и
устанавливает значение атрибута name равным new_name. Этот метод
должен быть декорирован как property.
• Метод is_adult, который возвращает True, если возраст объекта больше
или равен 18, и False в противном случае. Этот метод должен быть
декорирован как staticmethod.
• Метод create_from_string, который принимает один параметр: s, и
создает и возвращает объект класса Person на основе строки s. Строка s
должна иметь формат “name-age-gender”, где name - имя, age - возраст и
gender - пол. Этот метод должен быть декорирован как classmethod.
"""

class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.is_adult(int(age))
        self._name = name
        self.age = age
        self.gender = gender

    def __str__(self)-> str:
        return f"{self._name} {self.age} {self.gender}"

    def get_name(self)-> str:
        return self._name

    @property
    def name(self)-> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @staticmethod
    def is_adult(age: int)-> bool:
        return age >= 18

    @classmethod
    def create_from_string(cls, s: str):
        name, age_str, gender = s.split("-")
        age =int(age_str)
        return cls(name, age, gender)


# persona = Person("Boris",21, "man")
# persona1 = Person("Nina",14, "man")
# persona2 = Person("Vera",16, "man")
# persona3 = Person("Anna",20, "man")
# persona4 = Person("Lesha",25, "man")
# persona5 = Person("Gena",29, "man")






