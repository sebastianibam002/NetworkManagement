import os
MEDIA_LOCATION = "/Users/sebastianibarramendez/dev/CarniceriaIbarra/SocialNetwork/NetworkManagement/Media/"
EXPORTS_LOCATION = "/Users/sebastianibarramendez/dev/CarniceriaIbarra/SocialNetwork/NetworkManagement/Exports/"

API_WORD_GENERATOR = "https://random-word-api.herokuapp.com/word"
API_WORD_DEFINITION = "https://api.dictionaryapi.dev/api/v2/entries/en/"
API_RECIPE_GENERATOR = "https://api.spoonacular.com/recipes/random?number=1&tags=meat&apiKey=fe91355b5a844bc28636de9c2f94d17f"
API_QUOTE_GENERATOR = "https://zenquotes.io/api/random"


MORNING = (7, 8)
AFTERNOON = (11, 15)
EVENING = (18, 20)


USERNAME = os.environ['IG_USERNAME_CI']
PASSWORD = os.environ['IG_PASSWORD_CI']