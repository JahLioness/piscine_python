from S1E9 import Character

class Baratheon(Character):
    """Class inheriting from abstract Class Character, representing the Baretheon family."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize the Baretheon character with a name and alive status (default True)."""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
    def __str__(self):
        """String representation of the Baratheon character."""
        return f"Baratheon: {self.family_name}, {self.eyes}, {self.hairs}"
    def __repr__(self):
        """String representation of the Baratheon character."""
        return "Baratheon ('{}', '{}', '{}')".format(self.family_name, self.eyes, self.hairs)
    def die(self):
        """Method to set the character's is_alive status to False."""
        self.is_alive = False


class Lannister(Character):
    """Class inheriting from abstract Class Character, representing the Lannister family."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize the Lannister character with a name and alive status (default True)."""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"
    def die(self):
        """Method to set the character's is_alive status to False."""
        self.is_alive = False
    def __str__(self):
        """String representation of the Lannister character."""
        return f"Lannister: {self.family_name}, {self.eyes}, {self.hairs}"
    def __repr__(self):
        """String representation of the Lannister character."""
        return "Lannister ('{}', '{}', '{}')".format(self.family_name, self.eyes, self.hairs)
    @staticmethod
    def create_lannister(first_name: str, is_alive: bool = True):
        """Method to create a new Lannister character."""
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        return Lannister(first_name, is_alive)
