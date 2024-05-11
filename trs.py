from PIL import Image, ImageDraw, ImageFont

font_prefix = "C:\Windows\Fonts\\"

def doshit(id, *args, **kwargs):
    # print(id)
    # print(type(args), args)
    # print(type(kwargs), kwargs)

    category_font = ImageFont.truetype(f"C:\Windows\Fonts\BRLNSDB.TTF", 20)
    product_font = ImageFont.truetype(f"C:\Windows\Fonts\BRLNSDB.TTF", 15)

doshit(1, True, somestuff=False)