import sys
from ft_filter import ft_filter


def word_length(word, length) -> bool:
    """Return True if the length of the word is greater than the specified length."""
    return len(word) > length


def main():
    """Main function to execute the filtering of words based on their length, then print the resulting list."""
    try:
        assert len(sys.argv) == 3 and\
            (type(sys.argv[1]) is str and
                all(c.isdigit() for c in sys.argv[2])), \
            "AssertionError: the arguments are bad"
        myList = ft_filter(lambda word: word_length(word, int(sys.argv[2])),
                           sys.argv[1].split())
        print(myList)
    except AssertionError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
