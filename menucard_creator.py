from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os
import platform

from subtle_defs import *

MENU = {
     "BIRIYANI": {
         "Chicken Biriyani": 120,
         "Mutton Biriyani": 160,
         "Egg Biriyani": 80,
         "Aloo Biriyani": 70,
     },
     "CHINESE":{
         "Chicken Chowmein": 70,
         "Veg Chowmein": 70,
         "Mixed Chowmein": 70,
         "Fried Rice": 70,
         "Chilli Chicken": 100,
     },
     "THALI":{
         "Veg Thali": 40,
         "Chicken Thali": 50,
         "Egg Thali": 35,
     },
     "NONE":{
         "Ghoogni": 10,
         "Roti": 5,
         "Aloo Bhaja": 5,
     },
     "ALT":{
         "Ghoogni": 10,
         "Roti": 5,
         "Aloo Bhaja": 5,
         "Aloo Bhaja2": 5,
         "Aloo Bhaja3": 5,
         "Aloo Bhaja4": 5,
         "Aloo Bhaja5": 5,
         "Aloo Bhaja7": 5,
         "Aloo Bhaja4": 5,
         "Aloo Bhaja4sdg": 5,
         "Aloo Bhaja4sdgag": 5,
         "Aloo Bhaja4sdgagfw": 5,
         "Aloo Bhaja4sdgagfwa": 5,
         "Aloo Bhaja4sdgagfwaa": 5,
         "Aloo B": 5,
         "Aloo Bs": 5,
         "Aloo B": 5,
         "Aloo Bgg": 5,
         "Aloo Beg": 5,
         "Aloo Bsd": 5,
     }
}


current_os = platform.system()

printC(current_os)
if current_os == "Windows":
    font_prefix = "C:\Windows\Fonts\\"
else:
    font_prefix = "/usr/share/fonts/truetype/freefont/"

FREE_SANS = ...
BRITANIC = f"{font_prefix}BRITANIC.ttf"
BERLIN_SANS_FB_demibold = "C:\Windows\Fonts\BRLNSDB.TTF"
BAHNSCHRIFT_regular = "C:\Windows\Fonts\\bahnschrift.ttf"

BASE_FONT = BAHNSCHRIFT_regular

def generateMenuCard(MENU, path):

    WIDTH = 1275
    HEIGHT = 1650

    img = Image.new('RGB', (WIDTH, HEIGHT), color=(16, 16, 16))
    draw = ImageDraw.Draw(img)

    #  HEADING SPACE TILL Y = 300


    font = ImageFont.truetype(BASE_FONT, 90)
    # font = ImageFont.truetype(f"{font_prefix}FreeSans.ttf", 90)
    draw.text((40, 80), "KIDEY's Menu", font=font, fill=(255, 87, 51), stroke_fill=(255, 87, 51), stroke_width=2)

    font = ImageFont.truetype(BASE_FONT, 30)
    # font = ImageFont.truetype(f"{font_prefix}FreeSans.ttf", 30)
    todays_date = (datetime.today().strftime("%d.%m.%Y"))
    draw.text((WIDTH-380, 195), f"Generated on: {todays_date}", font=font, fill="grey", stroke_fill=(218, 165, 32), stroke_width=0)
    font = ImageFont.truetype(BASE_FONT, 35)
    # font = ImageFont.truetype(f"{font_prefix}FreeSans.ttf", 35)
    draw.text((WIDTH-450, 40), "ORDER NOW: 74074 89666", font=font, fill="yellow", stroke_fill="yellow", stroke_width=1)
    draw.text((WIDTH-215, 80), "95477 70599", font=font, fill="yellow", stroke_fill="yellow", stroke_width=1)
    draw.text((WIDTH-215, 120), "99329 65153", font=font, fill="yellow", stroke_fill="yellow", stroke_width=1)

    draw.line([(0, 230), (WIDTH, 230)], fill =(133, 138, 36), width = 7)

    #  HEADING DONE



    YCURSOR = 300
    CATEGORY_HEIGHT = 40
    PRODUCT_HEIGHT = 35


    
    category_font = ImageFont.truetype(BASE_FONT, CATEGORY_HEIGHT)
    product_font = ImageFont.truetype(BASE_FONT, PRODUCT_HEIGHT)
    # category_font = ImageFont.truetype(f"{font_prefix}FreeSans.ttf", CATEGORY_HEIGHT)
    # product_font = ImageFont.truetype(f"{font_prefix}FreeSans.ttf", PRODUCT_HEIGHT)


    for category in MENU:
        #  WRITE CATEGORY
        if category == "NONE":
            draw.text((50, YCURSOR), "OTHER ITEMS", font=category_font, fill=(127, 255, 0), stroke_fill=(127, 255, 0), stroke_width=2)
        else:
            draw.text((50, YCURSOR), category, font=category_font, fill=(127, 255, 0), stroke_fill=(127, 255, 0), stroke_width=2)

        YCURSOR += CATEGORY_HEIGHT + 10

        PRODUCTS = MENU[category]
        for product in PRODUCTS:
            draw.text((100, YCURSOR), product, font=product_font, fill=(135, 206, 235), stroke_fill=(135, 206, 235), stroke_width=0)
            draw.text((WIDTH-200, YCURSOR), '₹'+str(PRODUCTS[product])+'/-', font=product_font, fill=(218, 165, 32), stroke_fill=(218, 165, 32), stroke_width=0)
            

            YCURSOR += PRODUCT_HEIGHT + 10
        YCURSOR += 5


    savename = f"menucard.jpg"
    savedir = os.path.join(path, savename)
    img.save(savedir)

    print("SAVED!")
    return savedir

generateMenuCard(MENU, '.')