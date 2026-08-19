import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random 15-character alphanumeric ID."""
    return ''.join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Represents a student with a name, age, and unique ID."""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)
    def __post_init__(self):
        self.login = self.name[0].upper() + self.surname.lower()
