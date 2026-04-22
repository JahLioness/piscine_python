import sys

if len(sys.argv) == 1:
    sys.exit(0)

try:
    assert len(sys.argv) == 2, "AssertionError: more than one argument is provided"
    assert sys.argv[1][0] == '-' and sys.argv[1][1:].isdigit() or sys.argv[1].isdigit(), "AssertionError: argument is not an integer"
except AssertionError as e:
    print(e)
    sys.exit(1)

if (int(sys.argv[1]) % 2 == 0):
    print(f"I'm Even")
else:
    print(f"I'm Odd")