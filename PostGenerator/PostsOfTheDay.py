from PostGenerator.Constants import AFTERNOON, EVENING, MORNING
from .QuoteOfTheDay import QuoteOfTheDay
from .WordOfTheDay import WordOfTheDay
from .RecipeOfTheDay import RecipeOfTheDay
import datetime


"""
This class would creatre the three posts of the day
"""
class PostsOfTheDay():

    def __init__(self) -> None:
         self.quote_of_the_day = QuoteOfTheDay()
         self.word_of_the_day = WordOfTheDay()
         self.recipe_of_the_day = RecipeOfTheDay()
         self.location_files = []
         self.current_one = ""




    """
    This function would retrieve information from the
    APIS and fill the attributes
    """
    def fill_with_information(self, time: datetime.datetime):
        # Morning 6 < time.hour < 8
        if time.hour > MORNING[0] and time.hour < MORNING[1]:
            self.quote_of_the_day.retrieve_data_api()
            self.quote_of_the_day.display_information()
        # Lunch 11 < time.hour <  14
        elif time.hour > AFTERNOON[0] and time.hour < AFTERNOON[1]:
            self.word_of_the_day.retrieve_data_api()
            self.recipe_of_the_day.display_information()
        # Evening 18  < time.hour < 20
        elif time.hour > EVENING[0] and time.hour < EVENING[1]:
            self.recipe_of_the_day.retrieve_data_api()
            self.word_of_the_day.display_information()

    """
    Creates the posts of the day
    """
    def generate_posts(self, time: datetime.datetime):
        # Morning 6 < time.hour < 8
        if time.hour > MORNING[0] and time.hour < MORNING[1]:
            self.quote_of_the_day.generate_post()
            self.current_one = self.quote_of_the_day.get_location_export()
        # Lunch 11 < time.hour <=  14
        elif time.hour > AFTERNOON[0] and time.hour < AFTERNOON[1]:
            self.word_of_the_day.generate_post()
            self.current_one = self.recipe_of_the_day.get_location_export()
        # Evening 18  < time.hour < 20
        elif time.hour > EVENING[0] and time.hour < EVENING[1]:
            self.recipe_of_the_day.generate_post()
            self.current_one = self.word_of_the_day.get_location_export()
        self.location_files = [self.quote_of_the_day.get_location_export(), self.recipe_of_the_day.get_location_export(), self.word_of_the_day.get_location_export()]


    """
    Getters for each of the posts
    """
    def get_quote_of_the_day_location(self) -> str:
        return self.location_files[0]
    def get_recipe_of_the_day_location(self) -> str:
        return self.location_files[1]
    def get_word_of_the_day_location(self) -> str:
        return self.location_files[2]

    """
    Returns the one that is already created the location link of the export
    """
    def get_available_one(self):
        for element in self.location_files:
            if element != "":
                return element