def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate and print basic statistics for the given numerical data.

    Parameters:
    *args: Variable length argument list of numerical values.
    **kwargs: Arbitrary keyword arguments (not used in this function).

    Returns:
    None
    """
    if not args:
        print("No data provided.")
        return
    