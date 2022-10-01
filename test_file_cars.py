# class Cars:
#     def __init__(self, name, color, year, crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.crashed = crashed
#
#     def drive(self):
#         print(self.name + ' Driving ')
#
#     def change_color(self, new_color):
#         self.color = new_color
#         print(new_color)
#
#     wheels_number = 4
#
# opel = Cars('Opel Vectra', 'red', '1999', True)
#
# opel.drive()
# opel.change_color('yellow')
# print(opel.wheels_number)
# <--------------------------------------->
class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.circumference = 2 * self.pi * self.radius

    def area(self):
        return self.pi * self.radius**2

    # def circumference(self):
    #     return 2 * self.pi * self.radius

circle1 = Circle(3)
print(circle1.area())
print(circle1.circumference)