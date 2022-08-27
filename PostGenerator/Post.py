from Constants import *
from PIL import Image, ImageFont, ImageDraw 

class Post():
    def __init__(self):
        self.msg = ""
        self.image = ""
        # QuoteOfDay, RecipeOfDay, WordOfDay

    def set_msg(self, text: str) -> None:
        self.msg = text
    
    def set_image(self, name_file: str) -> None:
        self.image = f"{MEDIA_LOCATION}{name_file}"

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
        my_image.save(f"{EXPORTS_LOCATION}{export_name}.png")


if __name__ == "__main__":
    myPost = Post()
    myPost.set_msg("Hola mundo")
    myPost.set_image("WordOfDayTemplate.png")
    myPost.get_text_inside_image_post()

        