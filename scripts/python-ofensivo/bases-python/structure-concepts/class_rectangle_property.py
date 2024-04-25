#!/usr/bin/env python3


class Rectangle:

    def __init__(self, width, height):

        self.width=width
        self.height=height

    """Decorator for rectangles""" 
    @property
    def area(self): 
         area = self.width * self.height
         return f"\n[+] The area of the rectangle is: {area}"
    def __str__(self) -> str:
        return f"The object rectangle has [width: {self.width}] [height: {self.height}]"

rect1 = Rectangle(10, 20)
print(rect1)
#? the decorator for rectangles - we don need to call the method. Just execute the function 
print(rect1.area)