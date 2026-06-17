from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character in the Game of Thrones universe."""
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize the character with a name and alive status."""
        pass
    @abstractmethod
    def die(self):
        """Method to update the character's is_alive status."""
        pass

class Stark(Character):
    """Class inheriting from abstract Class Character, representing the Stark family."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize the Stark character with a name and alive status (default True)."""
        self.first_name = first_name
        self.is_alive = is_alive
    def die(self):
        """Method to set the character's is_alive status to False."""
        self.is_alive = False