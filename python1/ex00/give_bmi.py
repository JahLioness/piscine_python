def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate the Body Mass Index (BMI) for a list of heights and weights.
    Parameters:
        height (list of int or float): A list of heights in meters.
        weight (list of int or float): A list of weights in kilograms.
    Returns:
    list of int or float:
        A list of BMI values corresponding to each height and weight pair.
    """
    try:
        if len(height) != len(weight):
            raise ValueError("Height and weight lists"
                             " must be of the same length.")
        bmi_values = []
        for h, w in zip(height, weight):
            if h <= 0:
                raise ValueError("Height must be greater than zero.")
            bmi = w / (h ** 2)
            bmi_values.append(bmi)
        return bmi_values
    except Exception as e:
        print(f"Error calculating BMI: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit to the BMI values and
        return a list of booleans indicating
        whether each BMI exceeds the limit."""
    try:
        if not bmi:
            raise ValueError("BMI list cannot be empty.")
        if limit <= 0:
            raise ValueError("Limit must be greater than zero.")
        return [value > limit for value in bmi]
    except Exception as e:
        print(f"Error applying limit: {e}")
        return []
