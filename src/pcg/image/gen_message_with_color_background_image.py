from PIL import Image, ImageDraw, ImageFont
import random

# define the text
text = "Hello World"

# define the font
font = ImageFont.truetype("Chalkduster.ttf", 36)

# calculate the size of the text
left, top, right, bottom = font.getbbox(text)

text_width = abs(right - left)
text_height = abs(top - left)

# generate a random RGB color
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

# create an image with the random color
image = Image.new("RGB", (300, 300), (r, g, b))

# create an ImageDraw object
draw = ImageDraw.Draw(image)

# draw the text on the image
draw.text((0, 0), text, font=font)

# save the image
image.save("hello_world.png")
