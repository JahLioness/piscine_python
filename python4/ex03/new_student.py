import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random 15-character alphanumeric ID."""
    return ''.join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Represents a student with a name, age, and unique ID."""
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.active = True
        self.login =  self.name[0].upper() + self.surname.lower()
        self.id = field(default_factory=generate_id)
        print(f"Student (name='{self.name}', surname='{self.surname}', active={self.active}, login='{self.login}', id='{self.id}')")