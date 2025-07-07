"""Напишите класс Rectangle, который имеет атрибуты: width (ширина) и
height (высота). Класс должен иметь следующие методы:
• Конструктор, который принимает два параметра: width и height, и
инициализирует соответствующие атрибуты.
• Метод str, который возвращает строковое представление объекта класса
Rectangle в формате “Прямоугольник с шириной width и высотой
height”.
• Метод get_area, который возвращает площадь прямоугольника.
• Метод get_perimeter, который возвращает периметр прямоугольника.
• Метод is_square, который возвращает True, если прямоугольник является
квадратом, и False в противном случае. Этот метод должен быть
декорирован как property."""


class Rectangle:
    def __init__(self, width: int | float, height: int | float):
        self._validate_dimension(width, height)
        self._width = width
        self._height = height

    @staticmethod
    def _validate_dimension(width: int, height: int):
        if not (isinstance(width, int) and isinstance(height, int)):
            raise TypeError("Значения должны быть числом")

        if width < 0 or height < 0:
            raise ValueError("Значение должно быть положительными")

    def __str__(self) -> str:
        return f"Прямоугольник с шириной: {self._width}, и высотой: {self._height}"

    def get_area(self) -> int:
        return self._width * self._height

    def get_perimeter(self) -> int:
        return 2 * (self._width + self._height)

    @property
    def is_square(self) -> bool:
        return self._width == self._height


try:
    a = Rectangle(100, 100)
    b = Rectangle(40, 100)

    print(a)
    print(b)
    print(a.get_area())
    print(b.get_perimeter())
    print(a.is_square)
    print(b.is_square)

except (ValueError, TypeError) as e:
    print(f"Ошибка: {e}")
