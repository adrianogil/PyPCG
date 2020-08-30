import numpy as np
import random
import json
import cv2
import sys


PI = 3.14

na = np.array

a = na([0.2, 0.2, 0.2])
b = na([0.8, 0.8, 0.8])
c = na([
    random.uniform(0, 1),
    random.uniform(0, 1),
    random.uniform(0, 1)
])
d = na([
    random.uniform(0, 1),
    random.uniform(0, 1),
    random.uniform(0, 1)
])


def gen_color(t):
    # https://www.iquilezles.org/www/articles/palettes/palettes.htm
    return 255 * (a + b * np.cos(2.0 * PI * (c * t + d)))


def gen_image_palette(image_path, width, height, total_x_colors, total_y_colors):
    color_section_x = int(width / total_x_colors)
    color_section_y = int(height / total_y_colors)

    image = np.ones((height, width, 3))

    for i in range(total_x_colors):
        for j in range(total_y_colors):
            t = i + j * total_x_colors
            t /= (total_x_colors * total_y_colors)
            image[j * color_section_y:(j + 1) * color_section_y, i * color_section_x:(i + 1) * color_section_x, :] = gen_color(t)

    cv2.imwrite(image_path, image)

    generation_data = {
        "image_name": image_path,
        "width": width,
        "height": height,
        "total_x_colors": total_x_colors,
        "total_y_colors": total_y_colors,
        "color_palette_config": {
            "a": a.tolist(), "b": b.tolist(), "c": c.tolist(), "d": d.tolist()
        }
    }

    with open(image_path + ".json", 'w') as json_file:
        json.dump(generation_data, json_file)


if __name__ == '__main__':
    image_path = sys.argv[1]
    width = int(sys.argv[2])
    height = int(sys.argv[3])

    total_x_colors = int(sys.argv[4])
    total_y_colors = 1

    if len(sys.argv) > 5:
        total_y_colors = int(sys.argv[5])
    gen_image_palette(image_path, width, height, total_x_colors, total_y_colors)
