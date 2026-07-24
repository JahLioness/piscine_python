from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class inheriting from Baratheon and Lannister, representing a King character."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize the King character with a name and alive status (default True)."""
        super().__init__(first_name, is_alive)
    def __str__(self):
        """String representation of the King character."""
        return f"King: {self.family_name}, {self.eyes}, {self.hairs}"
    def __repr__(self):
        """String representation of the King character."""
        return "King ('{}', '{}', '{}')".format(self.family_name, self.eyes, self.hairs)
    def set_eyes(self, eyes: str):
        """Method to set the King's eye color."""
        self.eyes = eyes
    def set_hairs(self, hairs: str):
        """Method to set the King's hair color."""
        self.hairs = hairs
    def get_eyes(self):
        """Method to get the King's eye color."""
        return self.eyes
    def get_hairs(self):
        """Method to get the King's hair color."""
        return self.hairs