from load_image import load_img
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def zoom(array: np.ndarray) -> np.ndarray:
    """Zooms in on an image using slicing,
    interpolation, and grayscale conversion.
    Parameters:
        array (np.ndarray): The input image array.
    Returns:
        np.ndarray: The zoomed-in image array.
    """
    if array is None or not isinstance(array, np.ndarray):
        raise ValueError("Input must be a valid NumPy array.")
    height, width = array.shape[:2]
    crop_size = max(1, min(height, width) // 2)
    start_y = (height - crop_size) // 2
    start_x = (width - crop_size) // 2
    sliced_array = array[start_y:start_y + crop_size,
                         start_x:start_x + crop_size]
    scaled_array = np.array(
        Image.fromarray(sliced_array).resize((crop_size, crop_size),
                                             Image.BICUBIC)
    )
    gray_array = np.array(
        Image.fromarray(sliced_array).resize((crop_size, crop_size),
                                             Image.BICUBIC).convert("L")
    )
    print(f"New shape after zoom: {scaled_array.shape} or {gray_array.shape}")
    return gray_array


def main():
    try:
        img = load_img("./animal.jpeg")
        print(img)
        zoomed_img = zoom(img)
        print(zoomed_img)
        plt.imshow(zoomed_img, cmap="gray")
        plt.xticks(np.arange(0, zoomed_img.shape[1] + 1, 50))
        plt.yticks(np.arange(0, zoomed_img.shape[0] + 1, 50))
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
