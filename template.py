from PIL import Image, ImageDraw, ImageFont


image = Image.open(f"images/mem1.jpg")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("fonts/font_2.ttf", 24, encoding="Windows-1251")
font2 = ImageFont.truetype("fonts/font_2.ttf", 72, encoding="Windows-1251")

draw.text((140, 20), "Текст 1", font=font, fill="black")
draw.text((140, 110), "Текст 2", font=font, fill="black")
draw.text((10, 50), "1", font=font2, fill="white")
name = "images/mem1_text.jpg"
image.save(name)

image = Image.open(f"images/mem2.jpg")
draw = ImageDraw.Draw(image)
draw.text((140, 25), "Текст 1", font=font, fill="black")
draw.text((140, 150), "Текст 2", font=font, fill="black")
draw.text((10, 60), "2", font=font2, fill="white")
name = "images/mem2_text.jpg"
image.save(name)

image = Image.open(f"images/mem3.jpg")
draw = ImageDraw.Draw(image)
draw.text((150, 5), "Текст 1", font=font, fill="black")
draw.text((150, 150), "Текст 2", font=font, fill="black")
draw.text((10, 100), "3", font=font2, fill="white")
name = "images/mem3_text.jpg"
image.save(name)

image = Image.open(f"images/mem4.jpg")
draw = ImageDraw.Draw(image)
draw.text((10, 5), "Текст 1", font=font, fill="black")
draw.text((10, 110), "Текст 2", font=font, fill="black")
draw.text((190, 80), "4", font=font2, fill="white")
name = "images/mem4_text.jpg"
image.save(name)

image = Image.open(f"images/mem5.jpg")
draw = ImageDraw.Draw(image)
draw.text((10, 70), "Текст 1", font=font, fill="black")
draw.text((230, 70), "Текст 2", font=font, fill="black")
draw.text((200, 170), "5", font=font2, fill="white")
name = "images/mem5_text.jpg"
image.save(name)

image = Image.open(f"images/mem6.jpg")
draw = ImageDraw.Draw(image)
draw.text((10, 200), "Текст 1", font=font, fill="black")
draw.text((200, 200), "Текст 2", font=font, fill="black")
draw.text((120, 100), "6", font=font2, fill="black")
name = "images/mem6_text.jpg"
image.save(name)