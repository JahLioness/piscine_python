def ft_filter(function, iterable) -> iter:
    """Filter elements from an iterable using a list comprehension expression."""
    return [element for element in iterable if function(element)]
