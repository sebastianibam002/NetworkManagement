from .Post import Post
import requests
from .Constants import *
from googletrans import Translator
import time

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
class WordOfTheDay(Post):
    def __init__(self) -> None:
        super().__init__()
        self.image = f"{MEDIA_LOCATION}WordOfDayTemplate.png"


    """
    Retrieves the data from the API and fill the attributes
    """
    def retrieve_data_api(self):
        response = requests.get(API_WORD_GENERATOR)
        response_json = response.json()
        word = response_json[0]
        definition_link = f"{API_WORD_DEFINITION}{word}"
        response_definition = requests.get(definition_link)
        response_defintion_json = response_definition.json()
        find_definition = False
        while not find_definition:
            print(response_defintion_json)
            if len(response_defintion_json) == 1:
                # there is deifnition to that word
                definition = response_defintion_json[0]['meanings'][0]['definitions'][0]['definition']
                find_definition = True
            else:
                # there is not definition to thalwn t word
                time.sleep(3)
                response = requests.get(API_WORD_GENERATOR)
                response_json = response.json()
                word = response_json[0]
                definition_link = f"{API_WORD_DEFINITION}{word}"
                response_definition = requests.get(definition_link)
                response_defintion_json = response_definition.json()
            

        # translate
        translator = Translator()
        word_translated = translator.translate(word, dest="es").text
        definition_translated = translator.translate(definition, dest="es").text
        self.msg = f"{word_translated.capitalize()}\n\n{fix_text(definition_translated, 60)}"


    """
    Generate the post image
    """
    def generate_post(self) -> None:
        self.get_text_inside_image_post(200, 400, 24, "WordPost")
        self.location_export = f"{EXPORTS_LOCATION}WordPost.jpeg"

if __name__ == "__main__":
    wordDay = WordOfTheDay()
    wordDay.retrieve_data_api()
    wordDay.generate_post()