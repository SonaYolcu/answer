from math import pi


def area_circle(radius):
    if radius > 0:
        return pi*radius**2
    else:
        return 'Радиус должен быть положительным'


def area_triangle(a, b, c):
    if test_triangle(a, b, c):
        if a>0 and b>0 and c>0:
            p = (a + b + c)/2
            return ((p-a)*(p-b)*(p-c))**0.5
        else:
            return 'Стороны треугольника должны быть положительным'
    else:
        return 'Такой треугольник не существует!'

def test_triangle(a, b, c):
    return  a+b>c and a+c>b and b+c>a

def test_right_triangle_(a, b, c):
    if a>0 and b>0 and c>0:
        if test_triangle(a, b, c):
            if c**2==a**2 + b**2 or b**2==a**2 + c**2 or a**2==c**2 + b**2:
                return True,'Треугольник является прямыугольным'
            else:
                return False,'Треугольник не является прямыугольным'
        else:
            return 'Такой треугольник не существует!'

def area_geometric_shapes(option):
    if option == 1:
        radius = float(input('Введите радиус: '))
        return area_circle(radius)

    if option == 2:
        a = float(input('Введите сторону a: '))
        b = float(input('Введите сторону b: '))
        c = float(input('Введите сторону c: '))
        if test_triangle(a, b, c):
            option = int(input('Введите номер действий:1 - вычислить площадь треугольника, 2 - проверить, является ли треугольник прямоугольным: ?'))
            if option == 1:
                return area_triangle(a, b, c)
            if option == 2:
                return test_right_triangle_(a, b, c)
            else:
                return 'Не существует дейсвия'
        else:
            return 'Такой треугольник не существует'

def start():
    num = int(input(f"""Существующие фигуры: 
        1 - круг 
        2 - треугольник 

Введите номер фигуры: """))

    answer = area_geometric_shapes(num)
    if type(answer) != str:
        print(f"Площадь: {answer}")
    else:
        print(answer)

if __name__ == '__main__':
    start()