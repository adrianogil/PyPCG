from random import randint

import numpy as np
import cv2
import sys


if len(sys.argv) < 4:
    print("Usage: python gen_color_image.py <image_path> <width> <height> [total_x_colors] [total_y_colors]")
    sys.exit(1)

image_path = sys.argv[1]
width = int(sys.argv[2])
height = int(sys.argv[3])

total_x_colors = 1
total_y_colors = 1

if len(sys.argv) > 4:
    total_x_colors = int(sys.argv[4])

if len(sys.argv) > 5:
    total_y_colors = int(sys.argv[5])


def gen_random_color():
    """
    Generates a random RGB color.

    Returns:
        list: A list containing three integers representing the RGB values of the color.
    """
    return [randint(0, 255), randint(0, 255), randint(0, 255)]


color_section_x = int(width / total_x_colors)
color_section_y = int(height / total_y_colors)

image = np.ones((height, width, 3))

for i in range(total_x_colors):
    for j in range(total_y_colors):
        image[j * color_section_y:(j + 1) * color_section_y, i * color_section_x:(i + 1) * color_section_x, :] = gen_random_color()

cv2.imwrite(image_path, image)
