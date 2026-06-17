from load_image import load_img
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey, ft_display

array = load_img("landscape.jpg")
ft_display(array, "Original Image")
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)
print(ft_invert.__doc__)