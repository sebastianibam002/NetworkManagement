from Post import Post
import requests
from bs4 import BeautifulSoup
from Constants import *
from googletrans import Translator
from PIL import Image
"""
Given a string it splits the text each given amount
"""


def fix_text(text: str, how_long: int = 47) -> str:
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
Downloads an image from the internet
"""
def download_image(url_image: str,) -> None:
    stored_name = f"{MEDIA_LOCATION}recipe_example{url_image[-4::]}"

    img_data = requests.get(url_image).content
    with open(stored_name, 'wb') as handler:
        handler.write(img_data)
    return stored_name


"""
This would create a post of word of the day
"""


class RecipeOfTheDay(Post):
    def __init__(self) -> None:
        super().__init__()
        self.image = f"{MEDIA_LOCATION}RecipeOfDayTemplate.png"
        self.export_post = ""
        self.recipe_image = ""

    """
    Retrieves the data from the API and fill the attributes
    """

    def retrieve_data_api(self):
        response = requests.get(API_RECIPE_GENERATOR)
        response_json = response.json()
        soup = BeautifulSoup(
            response_json['recipes'][0]['instructions'], features="html.parser")
        text = soup.get_text()
        text = text.replace("\n", "")
        translator = Translator()
        title_translated = translator.translate(response_json['recipes'][0]['title'], dest="es").text
        # cut the text if it is greater than a value
        if len(text) > 921:
            text = f"{text[:921]}.."

        result = translator.translate(text, dest='es').text
        # remove the other words

        self.msg = f"{title_translated.capitalize()}\n\n{fix_text(result, 70)}"
        self.recipe_image = download_image(response_json['recipes'][0]['image'])


    """
    Pastes the image of the result recipe on top of the Post
    """
    def paste_image_post(self) -> None:
        post = Image.open(self.export_post)
        recipe_image = Image.open(self.recipe_image)
        resized_image = recipe_image.resize((415,415))
        post.paste(resized_image, (640, 374))
        post.save(f'{EXPORTS_LOCATION}RecipePostFinal.png')


    """
    Generate the post image
    """

    def generate_post(self) -> None:
        self.get_text_inside_image_post(77, 400, 16, "RecipePostTemp")
        self.export_post = f"{EXPORTS_LOCATION}RecipePostTemp.png"

if __name__ == "__main__":
    wordDay = RecipeOfTheDay()
    wordDay.retrieve_data_api()
    wordDay.generate_post()
    wordDay.paste_image_post()
