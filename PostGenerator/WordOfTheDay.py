from Post import Post
import requests
from bs4 import BeautifulSoup
from Constants import *


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
        self.export_post = ""


    """
    Retrieves the data from the API and fill the attributes
    """
    def retrieve_data_api(self):
        response = requests.get(API_WORD_GENERATOR)
        response_json = response.json()
        soup = BeautifulSoup(response_json['body']['DefinitionMD'], features="html.parser")
        text = soup.get_text()
        # remove the other words

        similar_pos = text.find("**")
        synonims_pos = text.find("##")
        where_to_end = 0
        if similar_pos == -1 or synonims_pos == -1:
            where_to_end = max(similar_pos, synonims_pos)
        else:
            where_to_end = min(similar_pos, synonims_pos)

        self.msg = f"{response_json['body']['Word'].capitalize()}\n\n{fix_text(text[:where_to_end - 1], 60)}"


    """
    Generate the post image
    """
    def generate_post(self) -> None:
        self.get_text_inside_image_post(200, 400, 24, "WordPost")
        self.export_post = "WordPost.png"

if __name__ == "__main__":
    wordDay = WordOfTheDay()
    wordDay.retrieve_data_api()
    wordDay.generate_post()