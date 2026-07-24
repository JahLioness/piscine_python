class calculator:
    """
    A simple calculator class that performs basic arithmetic operations on a list of numbers."""
    def __init__(self, object):
        self.object = object
    def __add__(self, object):
        """Add a number to each element in the list."""
        self.object = [x + object for x in self.object]
        print(f"{self.object}")
    def __mul__(self, object):
        """Multiply each element in the list by a number."""
        self.object = [x * object for x in self.object]
        print(f"{self.object}")
    def __sub__(self, object):
        """Subtract a number from each element in the list."""
        self.object = [x - object for x in self.object]
        print(f"{self.object}")
    def __truediv__(self, object):
        """Divide each element in the list by a number."""
        if object == 0:
            print("Error: Division by zero is not allowed.")
            return
        self.object = [x / object for x in self.object]
        print(f"{self.object}")