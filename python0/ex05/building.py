import sys


def count_characters(s) -> int:
    """Counts the number of characters in a string."""
    count = 0
    for char in s:
        count += 1
    return count


def count_uppercase(s) -> int:
    """Counts the number of uppercase letters in a string."""
    count = 0
    for char in s:
        if char.isupper():
            count += 1
    return count


def count_lowercase(s) -> int:
    """Counts the number of lowercase letters in a string."""
    count = 0
    for char in s:
        if char.islower():
            count += 1
    return count


def count_punctuation(s) -> int:
    """Counts the number of punctuation marks in a string. (.,;:!?)"""
    count = 0
    for char in s:
        if char in ".,;:!?":
            count += 1
    return count


def count_spaces(s) -> int:
    """Counts the number of spaces in a string."""
    count = 0
    for char in s:
        if char.isspace():
            count += 1
    return count


def count_digits(s) -> int:
    """Counts the number of digits in a string."""
    count = 0
    for char in s:
        if char.isdigit():
            count += 1
    return count


def main():
    """Main function to execute the character counting."""
    try:
        assert len(sys.argv) == 2 or len(sys.argv) == 1, \
            "AssertionError: more than one argument is provided"
        if len(sys.argv) == 1:
            str = input("What is the text to count?\n")
        else:
            str = sys.argv[1]
        print(f"The text contains {count_characters(str)} characters:")
        print(f"{count_uppercase(str)} upper letters")
        print(f"{count_lowercase(str)} lower letters")
        print(f"{count_punctuation(str)} punctuation marks")
        print(f"{count_spaces(str)} spaces")
        print(f"{count_digits(str)} digits")
    except AssertionError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
