from .Constants import *
from PIL import Image, ImageFont, ImageDraw
from datetime import datetime

class Post():
    def __init__(self):
        self.msg = ""
        self.image = ""
        self.location_export = ""
        self.time_stamp = datetime.now()
        # QuoteOfDay, RecipeOfDay, WordOfDay

    def get_location_export(self):
        return self.location_export

    def set_msg(self, text: str) -> None:
        self.msg = text
    
    def set_image(self, name_file: str) -> None:
        self.image = f"{MEDIA_LOCATION}{name_file}"

    """
    Displays the current message that is stored on the object
    """
    def display_information(self):
        print(f"Created on: {self.time_stamp}\n{'*'*20}\n{self.msg}")

    """
    Returns the post in a tuple with (text, image)
    """
    def get_text_image_post(self):
        return (self.msg, self.image)

    """
    Returns the post with the text inside of the image
    """
    def get_text_inside_image_post(self, x: int, y: int, size_letter: int, export_name: str):
        my_image = Image.open(self.image)
        # suggested size  24
        title_font = ImageFont.truetype('NetworkManagement/Fonts/BeVietnamPro-Regular.ttf', size_letter)
        image_editable = ImageDraw.Draw(my_image)
        # (x,y ) and color(R, G, B)
        image_editable.text((x,y), self.msg, (237, 230, 211), font=title_font)
        new_image = my_image.convert('RGB')
        new_image.save(f"{EXPORTS_LOCATION}{export_name}.jpeg")


if __name__ == "__main__":
    myPost = Post()
    myPost.set_msg("Hola mundo")
    myPost.set_image("WordOfDayTemplate.png")
    myPost.get_text_inside_image_post()

        