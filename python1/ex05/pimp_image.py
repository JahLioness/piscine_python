import numpy as np
import matplotlib.pyplot as plt


def ft_display(array, title: str):
    """Displays an image array.
    Parameters:
        array (np.ndarray): The input image array to be displayed.
        title (str): The title for the displayed image.
    Returns:
        None
    """
    if array is None or not isinstance(array, np.ndarray):
        raise ValueError("Input must be a valid NumPy array.")
    plt.imshow(array)
    plt.title(title)
    plt.axis('off')
    plt.show()


def ft_invert(array):
    """Inverts the colors of an image.
    Parameters:
        array (np.ndarray): The input image array.
    Returns:
        np.ndarray: The color-inverted image array.
    """
    if array is None or not isinstance(array, np.ndarray):
        raise ValueError("Input must be a valid NumPy array.")
    inverted_array = 255 - array
    ft_display(inverted_array, "Inverted Image")
    return inverted_array


def ft_red(array):
    """Extracts the red channel from an image.
    Parameters:
        array (np.ndarray): The input image array.
    Returns:
        np.ndarray: The red channel image array.
    """
    if array is None or not isinstance(array, np.ndarray):
        raise ValueError("Input must be a valid NumPy array.")
    red_array = array.copy()
    red_array[:, :, 1] = 0  # Set green channel to 0
    red_array[:, :, 2] = 0  # Set blue channel to 0
    ft_display(red_array, "Red Channel")
    return red_array


def ft_green(array):
    """Extracts the green channel from an image.
    Parameters:
        array (np.ndarray): The input image array.
    Returns:
        np.ndarray: The green channel image array.
    """
    if array is None or not isinstance(array, np.ndarray):
        raise ValueError("Input must be a valid NumPy array.")
    green_array = array.copy()
    green_array[:, :, 0] = 0  # Set red channel to 0
    green_array[:, :, 2] = 0  # Set blue channel to 0
    ft_display(green_array, "Green Channel")
    return green_array


def ft_blue(array):
    """Extracts the blue channel from an image.
    Parameters:
        array (np.ndarray): The input image array.
    Returns:
        np.ndarray: The blue channel image array.
    """
    if array is None or not isinstance(array, np.ndarray):
        raise ValueError("Input must be a valid NumPy array.")
    blue_array = array.copy()
    blue_array[:, :, 0] = 0  # Set red channel to 0
    blue_array[:, :, 1] = 0  # Set green channel to 0
    ft_display(blue_array, "Blue Channel")
    return blue_array


def ft_grey(array):
    """Converts an image to grayscale.
    Parameters:
        array (np.ndarray): The input image array.
    Returns:
        np.ndarray: The grayscale image array.
    """
    if array is None or not isinstance(array, np.ndarray):
        raise ValueError("Input must be a valid NumPy array.")
    grey_array = np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])
    grey_array = grey_array.astype(np.uint8)
    grey_array = np.stack((grey_array, grey_array, grey_array), axis=-1)
    ft_display(grey_array, "Grayscale Image")
    return grey_array.astype(np.uint8)
