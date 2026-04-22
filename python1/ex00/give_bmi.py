def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate the Body Mass Index (BMI) for a list of heights and weights.

    Parameters:
    height (list of int or float): A list of heights in meters.
    weight (list of int or float): A list of weights in kilograms.

    Returns:
    list of int or float: A list of BMI values corresponding to each height and weight pair.
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")
    
    bmi_values = []
    for h, w in zip(height, weight):
        if h <= 0:
            raise ValueError("Height must be greater than zero.")
        bmi = w / (h ** 2)
        bmi_values.append(bmi)
    
    return bmi_values


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit to the BMI values and return a list of booleans indicating whether each BMI exceeds the limit."""
    return [value > limit for value in bmi]
