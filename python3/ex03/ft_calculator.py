class calculator:
    """
    A simple calculator class that performs basic arithmetic operations on a list of numbers."""
    def __init__(self, object):
        self.object = object
    def __add__(self, object):
        print(f"{[x + object for x in self.object]}")
        self.object = [x + object for x in self.object]
    def __mul__(self, object):
        print(f"{[x * object for x in self.object]}")
        self.object = [x * object for x in self.object]
    def __sub__(self, object):
        print(f"{[x - object for x in self.object]}")
        self.object = [x - object for x in self.object]
    def __truediv__(self, object):
        if object == 0:
            print("Error: Division by zero is not allowed.")
            return
        print(f"{[x // object for x in self.object]}")
        self.object = [x // object for x in self.object]