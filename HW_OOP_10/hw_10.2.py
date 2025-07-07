'''
    Требуется проверить, возможно ли из представленных отрезков условной длины
сформировать треугольник. Для этого необходимо создать класс
TriangleChecker, принимающий только положительные числа. С помощью
метода is_triangle() возвращаются следующие значения (в зависимости от
ситуации):
– Ура, можно построить треугольник!;
– С отрицательными числами ничего не выйдет!;
– Нужно вводить только числа!;
– Жаль, но из этого треугольник не сделать
'''

class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def is_triangle(self) -> str:

        if not isinstance(self.a, int) or not isinstance(self.b, int) or not isinstance(self.c, int):
            return "– Нужно вводить только числа!"

        if  self.a < 0 or self.b < 0 or self.c < 0:
            return "– С отрицательными числами ничего не выйдет!"

        if self.a + self.b > self.c and self.b + self.c > self.a and self.c + self.a > self.b:
            return f"– Ура, можно построить треугольник!"
        else:
            return "– Жаль, но из этого треугольник не сделать"




triangle1 = TriangleChecker(5, 5, 3)
print(triangle1.is_triangle())