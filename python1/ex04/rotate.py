from load_image import load_img
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def zoom(array: np.ndarray) -> np.ndarray:
    """Zooms in on an image using slicing,
    interpolation, and grayscale conversion."""
    if array is None or not isinstance(array, np.ndarray):
        raise ValueError("Input must be a valid NumPy array.")
    height, width = array.shape[:2]
    crop_size = 400
    start_y = (height - crop_size) // 2
    start_x = (width - crop_size) // 2
    sliced_array = array[start_y:start_y + crop_size,
                         start_x:start_x + crop_size]
    gray_array = np.array(
        Image.fromarray(sliced_array).resize((400, 400),
                                             Image.BICUBIC).convert("L")
    )
    return gray_array


def rotate(array: np.ndarray) -> np.ndarray:
    """Rotates an image by 90 degrees.
        hsplit function will create a list of arrays by splitting
        the input array into equal parts along the horizontal axis.
        Then we convert the list of arrays into a NumPy array,
        which will have a shape that reflects the number of splits
        and the dimensions of each split.
        Parameters:
            array (np.ndarray): The input image array.
        Returns:
            np.ndarray: The rotated image array.
    """
    if array is None or not isinstance(array, np.ndarray):
        raise ValueError("Input must be a valid NumPy array.")
    transposed_array = np.hsplit(array, array.shape[1])
    transposed_array = np.array(transposed_array)
    print(f"Shape after hsplit: {transposed_array.shape}")
    return transposed_array


def main():
    try:
        img = load_img("./animal.jpeg")
        print(img)
        zoomed_img = zoom(img)
        transposed_img = rotate(zoomed_img)
        print(f"New shape after Transpose: {transposed_img.shape}")
        print(transposed_img)
        plt.imshow(transposed_img, cmap="gray")
        plt.xticks(np.arange(0, transposed_img.shape[1], 50))
        plt.yticks(np.arange(0, transposed_img.shape[0], 50))
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
