from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os
import platform

from subtle_defs import *

MENU = {
     "BIRIYANI": {
         "Chicken Biriyani": 150,
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
         "END": 500,
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





# def draw_heading(draw):
#     #  HEADING SPACE TILL Y = 300


#     font = ImageFont.truetype(BASE_FONT, 90)
    
#     # font = ImageFont.truetype(f"{font_prefix}FreeSans.ttf", 90)
#     draw.text((40, 80), "KIDEY's Menu", font=font, fill=(255, 87, 51), stroke_fill=(255, 87, 51), stroke_width=2)

#     font = ImageFont.truetype(BASE_FONT, 30)
#     # font = ImageFont.truetype(f"{font_prefix}FreeSans.ttf", 30)
#     todays_date = (datetime.today().strftime("%d.%m.%Y"))
#     draw.text((PAGE_WIDTH-380, 195), f"Generated on: {todays_date}", font=font, fill="grey", stroke_fill=(218, 165, 32), stroke_width=0)
#     font = ImageFont.truetype(BASE_FONT, 35)
#     # font = ImageFont.truetype(f"{font_prefix}FreeSans.ttf", 35)
#     draw.text((PAGE_WIDTH-450, 40), "ORDER NOW: 74074 89666", font=font, fill="yellow", stroke_fill="yellow", stroke_width=1)
#     draw.text((PAGE_WIDTH-215, 80), "95477 70599", font=font, fill="yellow", stroke_fill="yellow", stroke_width=1)
#     draw.text((PAGE_WIDTH-215, 120), "99329 65153", font=font, fill="yellow", stroke_fill="yellow", stroke_width=1)

#     draw.line([(0, 230), (PAGE_WIDTH, 230)], fill =(133, 138, 36), width = 7)

#     #  HEADING DONE

#     return draw



# def generateMenuCard(MENU, path):

#     draw = create_page()
    
#     category_font = ImageFont.truetype(BASE_FONT, CATEGORY_HEIGHT)
#     product_font = ImageFont.truetype(BASE_FONT, PRODUCT_HEIGHT)

#     page_count = 1

#     for category in MENU:
#         #  WRITE CATEGORY
#         if category == "NONE":
#             draw.text((50, YCURSOR), "OTHER ITEMS", font=category_font, fill=(127, 255, 0), stroke_fill=(127, 255, 0), stroke_width=2)
#         else:
#             draw.text((50, YCURSOR), category, font=category_font, fill=(127, 255, 0), stroke_fill=(127, 255, 0), stroke_width=2)

#         YCURSOR += CATEGORY_HEIGHT + 10

#         PRODUCTS = MENU[category]
#         for product in PRODUCTS:
#             draw.text((100, YCURSOR), product, font=product_font, fill=(135, 206, 235), stroke_fill=(135, 206, 235), stroke_width=0)
#             draw.text((PAGE_WIDTH-200, YCURSOR), '₹'+str(PRODUCTS[product])+'/-', font=product_font, fill=(218, 165, 32), stroke_fill=(218, 165, 32), stroke_width=0)
            

#             YCURSOR += PRODUCT_HEIGHT + 10
        
#             if YCURSOR >= PAGE_HEIGHT - 0.1 * PAGE_HEIGHT:
#                 print("NEXT PAGE")
#                 break
        
#         YCURSOR += 5



#     savename = f"menucard.jpg"
#     savedir = os.path.join(path, savename)
#     img.save(savedir)

#     print("SAVED!")
#     return savedir

# generateMenuCard(MENU, '.')



class MenuCardCreator():
    def __init__(self) -> None:
        
        self.BASE_FONT = BAHNSCHRIFT_regular
        self.PAGE_WIDTH = 1275
        self.PAGE_HEIGHT = 1650
        self.YCURSOR = 300

        self.CATEGORY_HEIGHT = 40
        self.PRODUCT_HEIGHT = 35
        self.PRODUCT_HEIGHT = 40

        self.MENU_COVER_PORTION = 0.87

        self.page_count = 1
        self.path = None
        
        self.img = None
        self.draw = None

        self.category_font = ImageFont.truetype(self.BASE_FONT, self.CATEGORY_HEIGHT)
        self.product_font = ImageFont.truetype(self.BASE_FONT, self.PRODUCT_HEIGHT)
        self.page_number_font = ImageFont.truetype(self.BASE_FONT, self.PRODUCT_HEIGHT)

    def generate_menu_card(self, MENU: dict, path: str = '.'):
        self.path = path

        self.create_page()


        for category in MENU:
            #  WRITE CATEGORY

            self.write_category(self.YCURSOR, category)
            self.YCURSOR += self.CATEGORY_HEIGHT + 10

            PRODUCTS = MENU[category]
            for product in PRODUCTS:
                self.write_product(product, PRODUCTS[product], self.YCURSOR)
                
                self.YCURSOR += self.PRODUCT_HEIGHT + 10
                if self.YCURSOR >= self.MENU_COVER_PORTION * self.PAGE_HEIGHT:
                    self.write_page_number()
                    self.save_img()
                    self.page_count += 1
                    self.create_page()

            self.YCURSOR += 5
            if self.YCURSOR >= self.MENU_COVER_PORTION * self.PAGE_HEIGHT:
                self.write_page_number()
                self.save_img()
                self.page_count += 1
                self.create_page()


        self.write_page_number()
        self.save_img()

    # Breakout Functions ---------------------------------------------------
    def create_page(self):
        self.img = Image.new('RGB', (self.PAGE_WIDTH, self.PAGE_HEIGHT), color=(16, 16, 16))
        self.draw = ImageDraw.Draw(self.img)

        self.draw_heading()
        
    def draw_heading(self):
        font = ImageFont.truetype(self.BASE_FONT, 90)

        self.draw.text((40, 80), "KIDEY's Menu", font=font, fill=(255, 87, 51), stroke_fill=(255, 87, 51), stroke_width=2)

        font = ImageFont.truetype(self.BASE_FONT, 30)
        todays_date = (datetime.today().strftime("%d.%m.%Y"))
        self.draw.text((self.PAGE_WIDTH-380, 195), f"Generated on: {todays_date}", font=font, fill="grey", stroke_fill=(218, 165, 32), stroke_width=0)
        font = ImageFont.truetype(self.BASE_FONT, 35)
        self.draw.text((self.PAGE_WIDTH-450, 40), "ORDER NOW: 74074 89666", font=font, fill="yellow", stroke_fill="yellow", stroke_width=1)
        self.draw.text((self.PAGE_WIDTH-215, 80), "95477 70599", font=font, fill="yellow", stroke_fill="yellow", stroke_width=1)
        self.draw.text((self.PAGE_WIDTH-215, 120), "99329 65153", font=font, fill="yellow", stroke_fill="yellow", stroke_width=1)

        self.draw.line([(0, 230), (self.PAGE_WIDTH, 230)], fill =(133, 138, 36), width = 7)

        self.YCURSOR = 300

    def write_category(self, cursor, category: str):
        if category == "NONE":
            self.draw.text((50, cursor), "OTHER ITEMS", font=self.category_font, fill=(127, 255, 0), stroke_fill=(127, 255, 0), stroke_width=2)
        else:
            self.draw.text((50, cursor), category, font=self.category_font, fill=(127, 255, 0), stroke_fill=(127, 255, 0), stroke_width=2)
    
    def write_product(self, product: str, price: int, cursor):
        self.draw.text((100, cursor), product, font=self.product_font, fill=(135, 206, 235), stroke_fill=(135, 206, 235), stroke_width=0)
        self.draw.text((self.PAGE_WIDTH-200, cursor), '₹'+str(price)+'/-', font=self.product_font, fill=(218, 165, 32), stroke_fill=(218, 165, 32), stroke_width=0)

    def write_page_number(self):
        self.draw.text((self.PAGE_WIDTH - 300, self.PAGE_HEIGHT - 100), f"Page {self.page_count}", font=self.page_number_font, fill=(135, 135, 0), stroke_fill=(135, 206, 235), stroke_width=0)


    def new_page(self):
        pass

    def save_img(self):
        savename = f"menucard_{self.page_count}.jpg"
        savedir = os.path.join(self.path, savename)
        self.img.save(savedir)

        print("SAVED!")


m = MenuCardCreator()
m.generate_menu_card(MENU)