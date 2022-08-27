from Post import Post
import requests
from Constants import *
from googletrans import Translator

"""
Given a string it splits the text each given amount
"""
def fix_text(text: str, how_long: int=47) -> str:
    queue = []
    counter = 1
    new_string = ""
    for character in text:
        if character == "\n":
            queue = []
            counter = 1
        elif counter == how_long:
            queue = []
            new_string += "-\n"
            counter = 1

        else:
            queue.append(character)
            counter += 1
        new_string += character
    return new_string

"""
This would create a post of word of the day
"""
class QuoteOfTheDay(Post):
    def __init__(self) -> None:
        super().__init__()
        self.image = f"{MEDIA_LOCATION}QuoteOfDayTemplate.png"

    """
    Retrieves the data from the API and fill the attributes
    """
    def retrieve_data_api(self):
        response = requests.get(API_QUOTE_GENERATOR)
        response_json = response.json()
        text = response_json[0]['q']
        translator = Translator()
        quote_translated = translator.translate(text, dest="es").text
        self.msg = f"{fix_text(quote_translated, 56)}\n\n{response_json[0]['a']}"



    """
    Generate the post image
    """
    def generate_post(self) -> None:
        self.get_text_inside_image_post(204, 524, 24, "QuotePost")

if __name__ == "__main__":
    wordDay = QuoteOfTheDay()
    wordDay.retrieve_data_api()
    wordDay.generate_post()