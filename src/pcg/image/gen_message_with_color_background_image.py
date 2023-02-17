from PIL import Image, ImageDraw, ImageFont
import random

# define the text
text = "Hello World"

# define the font
font = ImageFont.truetype("Chalkduster.ttf", 36)

# calculate the size of the text
left, top, right, bottom = font.getbbox(text)

text_width = abs(right - left)
text_height = abs(top - bottom)

# generate a random RGB color
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

# create an image with the random color
image_width = 300
image_height = 300
image = Image.new("RGB", (image_height, image_width), (r, g, b))

# create an ImageDraw object
draw = ImageDraw.Draw(image)

# Center text
text_pos_x = image_width / 2 - text_width / 2
text_pos_y = image_height / 2 - text_height / 2

# draw the text on the image
draw.text((text_pos_x, text_pos_y), text, font=font)

# save the image
image.save("hello_world.png")
