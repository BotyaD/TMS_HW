"""
Необходимо создать класс KgToPounds, в который принимает количество
килограмм, а с помощью метода to_pounds() они переводятся в фунты.
Необходимо закрыть доступ к переменной kg.
Также, реализовать методы:
- set_kg() - для задания нового значения килограммов (записывать только
числовые значения),
- get_kg() - для вывода текущего значения кг.
Во второй версии необходимо использовать декоратор property для создания
setter и getter взамен set_kg и get_kg.
"""


class KgToPounds:
    def __init__(self, kg = None):
        self.__kg = kg

    def to_pounds(self) -> float:
        if self.__kg is None:
            raise ValueError("Килограммы не заданы")
        return self.__kg * 2.20462

    @property
    def kg(self) -> int:
        return self.__kg

    @kg.setter
    def kg(self, kg) -> None:
        if not isinstance(kg, (int, float)):
            raise TypeError("Должно быть цифрой")
        if kg <= 0:
            raise ValueError("Значение должно быть больше 0")
        self.__kg = kg

mass = KgToPounds()
mass.kg = 5
print(mass.to_pounds())
print(mass.kg)