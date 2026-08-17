def square(x:int | float) -> int |float:
    """Returns the square of a number."""
    return x * x

def pow(x:int | float) -> int |float:
    """Returns the exponentiation of a number by itself."""
    return x ** x

def outer(x:int | float, function) -> object:
    """Returns a closure that applies the given function to a number."""
    count = 0
    def inner() -> int | float:
        nonlocal count
        if count == 0:
            count = x
        else:
            count = function(count)
        return count
    return inner
