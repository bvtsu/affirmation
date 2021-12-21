from Affirmations.Affirm import affirm
from Affirmations.AffirmationText import affirmations
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from random import choice
from random import random

import textwrap

def generate_meme(image_path: str, bottom_text='', font_path='./fonts/impact/impact.ttf', 
                    font_size=9, stroke_width=5):
    """
    From nikhilkumarsingh/MemeGenerator, bottom_text only
    """
    # load image
    im = Image.open(image_path)
    draw = ImageDraw.Draw(im)
    image_width, image_height = im.size

    # load font
    font = ImageFont.truetype(font=font_path, size=int(image_height * font_size) // 100)

    # text wrapping
    char_width, char_height = font.getsize('A')
    chars_per_line = image_width // char_width
    bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)

    # draw bottom lines
    y = image_height - char_height * len(bottom_lines) - 30
    for line in bottom_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill='white', font=font, stroke_width=stroke_width, stroke_fill='black')
        y += line_height

    # save meme
    im.save('meme-' + im.filename.split('/')[-1])

def affirmImg(frequency: float, imgurl: str):
    if frequency > 1 or frequency < 0:
        frequency = 1
    
    if frequency > random():
        bottom_text = choice(affirmations)
        generate_meme(imgurl, bottom_text=bottom_text)


    #def decorator(function):
    #    def wrapper(*args, **kwargs):
    #        if frequency > random():
    #            print(choice(affirmations))
    #        return function(*args, **kwargs)
    #    return wrapper
    #return decorator

if __name__ == "__main__":
    affirmImg(1, './idontalways.jpg')