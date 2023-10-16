#!/usr/bin/python3
""" define a rectangle class """
from models.base import Base


class Rectangle(Base):
    """ rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ the constructor for the rectangle """

        self.width = width
        self.height = height
        self.x = x
        selx.y = y
        super().__init__(id)

    @property
    def width(self):
        """ setter or getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ setter or getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x setter or getter method """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the rectangle area """
        return self.width * self.height

    def display(self):
        """ display rectangle """
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """ over riding for better string """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self.x,
                self.y,
                self.width,
                self.height)

    def update(self):
        """ update the args """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in ["id", "width", "height", "x", "y"]:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ return dictionary of Rectangle """
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
