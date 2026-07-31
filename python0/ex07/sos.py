import sys

NESTED_MORSE = {
    ' ': '/',
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'
}


def parse_args(str: str) -> bool:
    """Check if the input string contains only
     valid characters (alphanumerics and spaces)."""
    for c in str:
        if not (c.isalpha() or c.isspace() or c.isdigit()):
            return False
    return True


def main():
    """Main function to execute the conversion
     of a string to Morse code, then print the resulting Morse code."""
    try:
        assert len(sys.argv) == 2 and \
            parse_args(sys.argv[1]), "AssertionError: the argument is bad"
        for c in sys.argv[1].upper():
            print(NESTED_MORSE[c], end=" ")
        print()
    except AssertionError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
