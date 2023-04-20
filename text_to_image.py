from PIL import Image, ImageDraw, ImageFont

image = Image.open("images/meme.jpg")

draw = ImageDraw.Draw(image)

text = "meme text"

font = ImageFont.truetype("fonts/font.ttf", 24)

x = 150
y = 20

draw.text((x, y), text, font=font, fill="black")

image.save("images/output.jpg")