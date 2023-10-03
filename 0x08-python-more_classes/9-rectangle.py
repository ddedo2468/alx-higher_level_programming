#!/usr/bin/python3
""" Define Class Rectangle """


class Rectangle:
    """Defines A Rectangle"""
    print_symbol = '#'
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ construction function """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get the Rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ get the rectangle height """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculating rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ calculate rectangle primeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ refactor str for rectangle class """
        if self.__width == 0 or self.__height == 0:
            return ""
        row = [str(self.print_symbol) * self.__width] * self.__height
        return "\n".join(row)

    def __repr__(self):
        """ more readable string """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ mesaage when obj is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ compares 2 rectangles based on their areas """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """ creates a square """
        return cls(size, size)