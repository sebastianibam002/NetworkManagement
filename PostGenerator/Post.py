from msilib.schema import Media
from Constants import *
class Post():
    def __init__(self):
        self.msg = ""
        self.image = ""

    def set_msg(self, text: str) -> None:
        self.msg = text
    
    def set_image(self, name_file: str) -> None:
        self.image = f"{MEDIA_LOCATION}/{name_file}"

    """
    Returns the post in a tuple with (text, image)
    """
    def get_text_image_post(self):
        return (self.msg, self.image)

    """
    Returns the post with the text inside of the image
    """
    def get_text_inside_image_post(self):
        pass