"""
Дополнительное практическое задание по модулю: "Наследование классов."
Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
Задание "Они все так похожи":
2D? 3D? Даже 4D?.... Настолько глубоко мы заходить конечно же не будем, 4D подождёт, но вот с двумерными и трёхмерными
 фигурами можем поэкспериментировать.
Вы когда-нибудь задумывались как устроены графические библиотеки для языков программирования?
Безусловно, там выполняются огромные расчёты при помощи вашей видеокарты, но... Что лежит в основе удобного
 использования таких объектов?
По названию задачи можно понять, что все геометрические фигуры обладают схожими свойствами, такими как: длины сторон,
 цвет и др.
Давайте попробуем реализовать простейшие классы для некоторых таких фигур и при этом применить наследование (в будущем,
 изучая сторонние библиотеки, вы будете замечать схожие классы, уже написанные кем-то ранее):

Общее ТЗ:
Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать методами изменения
 размеров, цвета и т.д.
Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы взаимодействия (методы)
 - геттеры и сеттеры.

Подробное ТЗ:
Атрибуты класса Figure: sides_count = 0
Каждый объект класса Figure должен обладать следующими атрибутами:
Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
Атрибуты(публичные): filled(закрашенный, bool)
И методами:
Метод get_color, возвращает список RGB цветов.
Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений
 перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне
 от 0 до 255 (включительно).
Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
 предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые
 положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
Метод get_sides должен возвращать значение я атрибута __sides.
Метод __len__ должен возвращать периметр фигуры.
Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, то не
 изменять, в противном случае - менять.
Атрибуты класса Circle: sides_count = 1
Каждый объект класса Circle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
Атрибуты класса Triangle: sides_count = 3
Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
Атрибуты класса Cube: sides_count = 12
Каждый объект класса Cube должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure.
Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
Метод get_volume, возвращает объём куба.

ВАЖНО!
При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то создать
 массив с единичными сторонами и в том кол-ве, которое требует фигура.
Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]

Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
# Проверка периметра (круга), это и есть длина:
print(len(circle1))
# Проверка объёма (куба):
print(cube1.get_volume())

Выходные данные (консоль):
[55, 66, 77]
[222, 35, 130]
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[15]
15
216

Примечания (рекомендации):
Рекомендуется сделать дополнительные (свои проверки) работы методов объектов каждого класса.
Делайте каждый класс и метод последовательно и проверяйте работу каждой части отдельно.
Для проверки принадлежности к типу рекомендуется использовать функцию isinstance.
Помните, служебные инкапсулированные методы можно и нужно использовать только внутри текущего класса.
Вам не запрещается вводить дополнительные атрибуты и методы, творите, но не переборщите!
"""
import math


class Figure:
    sides_count = 0  # кол-во сторон

    def __init__(self, color=(0, 0, 0), *sides):
        if len(sides) != self.sides_count:
            self.__sides = [list(sides)[0]] * self.sides_count
        elif len(sides) == self.sides_count:
            self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False

    def get_color(self):  # возвращает список RGB цветов
        return self.__color

    def __is_valid_color(self, r, g, b):
        # проверяет корректность переданных значений перед установкой нового цвета
        # все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно)
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True
            else:
                return False

    def set_color(self, r, g, b):
        # принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
        # предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
        if self.__is_valid_color(r, g, b):
            self.__color.clear()
            self.__color.extend([r, g, b])
            return self.__color

    def __is_valid_sides(self, *sides):
        # принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и кол-во
        # новых сторон совпадает с текущим, False - во всех остальных случаях.
        if len(sides) != self.sides_count:
            return False
        return all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides(self):  # должен возвращать значение атрибута __sides
        return self.__sides

    def __len__(self):  # должен возвращать периметр фигуры.
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        # должен принимать новые стороны, если их кол-во != sides_count, то не изменять, в противном случае - менять.
        if len(new_sides) == self.sides_count:
            self.__sides.clear()
            self.__sides.extend(new_sides)
        return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        # __radius рассчитать исходя из длины окружности (одной единственной стороны).
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        # возвращает площадь круга (можно рассчитать как через длину, так и через радиус)
        square = self.__radius ** 2 * math.pi
        return square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = 0

    def get_square(self):
        # возвращает площадь треугольника. (можно рассчитать по формуле Герона)
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        half_per = (a + b + c) / 2
        square = math.sqrt((half_per * (half_per - a) * (half_per - b) * (half_per - c)))
        return square


class Cube(Figure):
    sides_count = 12

    # Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = [list(sides)[0]] * self.sides_count
        self.volume = 0

    def get_volume(self):  # возвращает объём куба.
        self.volume = self.get_sides()[0] ** 3
        return self.volume


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())
