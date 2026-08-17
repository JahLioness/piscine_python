def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate and print basic statistics for the given numerical data.

    Parameters:
    *args: Variable length argument list of numerical values.
    **kwargs: Arbitrary keyword arguments (not used in this function).

    Returns:
    None
    """
    arg_list = list(args)
    kwarg_list = list(kwargs.values())
    for value in kwarg_list:
        if value == "mean":
            if not arg_list:
                print("ERROR")
                continue
            mean = sum(arg_list) / len(arg_list)
            print(f"mean: {mean}")
        if value == "median":
            if not arg_list:
                print("ERROR")
                continue
            sorted_list = sorted(arg_list)
            n = len(sorted_list)
            if n % 2 == 1:
                median = sorted_list[n // 2]
            else:
                median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
            print(f"median: {median}")
        if value == "quartile":
            if not arg_list:
                print("ERROR")
                continue
            sorted_list = sorted(arg_list)
            n = len(sorted_list)
            q1_index = n // 4
            q3_index = 3 * n // 4
            if n % 4 == 0:
                q1 = (sorted_list[q1_index - 1] + sorted_list[q1_index]) / 2
                q3 = (sorted_list[q3_index - 1] + sorted_list[q3_index]) / 2
            else:
                q1 = sorted_list[q1_index]
                q3 = sorted_list[q3_index]
            print(f"quartile: [{q1}, {q3}]")
        if value == "std":
            if not arg_list:
                print("ERROR")
                continue
            mean = sum(arg_list) / len(arg_list)
            variance = sum((x - mean) ** 2 for x in arg_list) / len(arg_list)
            std_dev = variance ** 0.5
            print(f"std: {std_dev}")
        if value == "var":
            if not arg_list:
                print("ERROR")
                continue
            mean = sum(arg_list) / len(arg_list)
            variance = sum((x - mean) ** 2 for x in arg_list) / len(arg_list)
            print(f"var: {variance}")