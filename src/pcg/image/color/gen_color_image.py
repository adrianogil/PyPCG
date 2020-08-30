from random import randint

import numpy as np
import cv2
import sys


image_path = sys.argv[1]
width = int(sys.argv[2])
height = int(sys.argv[3])

total_x_colors = int(sys.argv[4])
total_y_colors = 1

if len(sys.argv) > 5:
    total_y_colors = int(sys.argv[5])


def gen_random_color():
    return [randint(0, 255), randint(0, 255), randint(0, 255)]


color_section_x = int(width / total_x_colors)
color_section_y = int(height / total_y_colors)

image = np.ones((height, width, 3))

for i in range(total_x_colors):
    for j in range(total_y_colors):
        image[j * color_section_y:(j + 1) * color_section_y, i * color_section_x:(i + 1) * color_section_x, :] = gen_random_color()

cv2.imwrite(image_path, image)
