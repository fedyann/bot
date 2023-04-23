from PIL import Image, ImageDraw, ImageFont
import sqlite3
from pathlib import Path



class CreateMem():
    def __init__(self, number, text1, text2):
        self.number = number
        self.text1 = text1
        self.text2 = text2
        self.con = sqlite3.connect("data/meme.db")
        self.cur = self.con.cursor()
        self.text()

    def multiline_text(self, text, max_line_len=15):
        words = text.split()
        lines = []
        line = ""
        for word in words:
            if len(line + word) + 1 > max_line_len:
                lines.append(line)
                line = ""
            if line:
                line += " "
            line += word
        if line:
            lines.append(line)
        return "\n".join(lines)
    def text(self):
        img = self.cur.execute(f"SELECT name from coordinates where id = {self.number}").fetchall()[0][0]
        image = Image.open(f"images/{img}")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("fonts/font_2.ttf", 18, encoding="Windows-1251")
        x1 = self.cur.execute(f"SELECT x1 from coordinates where id = {self.number}").fetchall()[0][0]
        y1 = self.cur.execute(f"SELECT y1 from coordinates where id = {self.number}").fetchall()[0][0]
        x2 = self.cur.execute(f"SELECT x2 from coordinates where id = {self.number}").fetchall()[0][0]
        y2 = self.cur.execute(f"SELECT y2 from coordinates where id = {self.number}").fetchall()[0][0]

        draw.text((x1, y1), self.multiline_text(self.text1), font=font, fill="black")
        draw.text((x2, y2), self.multiline_text(self.text2), font=font, fill="black")
        name = "images/output.jpg"
        image.save(name)
        return name


