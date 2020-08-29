from random import randint

import numpy as np
import cv2
import sys


image_path = sys.argv[1]
width = int(sys.argv[2])
height = int(sys.argv[3])

total_colors = int(sys.argv[4])


def gen_random_color():
    return [randint(0, 255), randint(0, 255), randint(0, 255)]


color_section = int(width / total_colors)

image = np.ones((width, height, 3))
for c in range(total_colors):
    image[:, c * color_section:(c + 1) * color_section, :] = gen_random_color()

cv2.imwrite(image_path, image)
