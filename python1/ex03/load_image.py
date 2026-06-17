import numpy as np
from PIL import Image


def load_img(path: str) -> np.array:
    """
    Loads an image from the specified path and returns it as a NumPy array.

    Args:
        path (str): The file path to the image.
        This can be an absolute or relative path.
    Returns:
        np.array: A NumPy array representing the image.
        The shape of the array will depend on the
        image dimensions and color channels.
    """
    try:
        if (not isinstance(path, str)):
            raise ValueError("Path must be a string.")
        img = Image.open(path)
        if (img is None):
            raise ValueError("Could not load image. \
                             Please check the file path.")
        elif (img.format not in ['JPEG', 'JPG']):
            raise ValueError("Unsupported image format.\
                            Supported formats are JPEG, PNG, BMP, and GIF.")
        img = img.convert('RGB')  # Ensure the image is in RGB format
        if (img is None):
            raise ValueError("Could not convert image to RGB format.")
        img_array = np.array(img)
        if (img_array is None):
            raise ValueError("Could not convert image to NumPy array.")
        print(f"The shape of the image is : {img_array.shape}")
        return img_array
    except Exception as e:
        print(f"Error loading image: {e}")
        return np.array([])
