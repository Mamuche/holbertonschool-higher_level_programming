#!/usr/bin/python3
"""create class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return the rectangle description"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width)
    
    """decorator for size"""
    @property
    def size(self):
        return self.width
    
    """setter for size"""
    @size.setter
    def size(self, value):
        self.validator(width=value)
        self.validator(height=value)
        self.width = value
        self.height = value
