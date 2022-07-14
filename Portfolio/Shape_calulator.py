# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 12:03:04 2022

@author: jindo
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width*self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        if max(self.width, self.height) > 50:
            return 'Too big for picture.'
        w = '*' * self.width
        h = 0
        picture = ""
        while h < self.height:
            picture += w + '\n'
            h += 1
        return picture

    def get_amount_inside(self, other):
        hori = int(self.width/other.width)
        vert = int(self.height/other.height)
        times = hori * vert
        return times


class Square(Rectangle):

    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def __repr__(self):
        return 'Square(side=' + str(self.width) + ')'


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

