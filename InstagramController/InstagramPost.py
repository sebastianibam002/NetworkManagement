"""
This class would be in charge of posting on instagram the three posts of the day
"""
from datetime import datetime
from PostGenerator.Constants import PASSWORD, USERNAME
from instagrapi import Client

MORNING = (7, 8)
AFTERNOON = (11, 15)
EVENING = (18, 20)

class InstagramPost():

    def __init__(self) -> None:
        self.location_file_post = ""


    """
        Post on the account the post
        given the 
        type: 0, 1 , 2 [morning, afternoon, evening]
        caption: caption text on the post
    """
    def post(self, time: datetime):
        cl = Client()
        cl.login(USERNAME, PASSWORD)
        caption = " #carnesmaduradas #lomadelbalsamo #chorizos #carnes #carniceria #carnesibarra"
        if time.hour > MORNING[0] and time.hour < MORNING[1]:
            caption = "Desde Carnes Ibarra le deseamos muy productiva mañana" + caption 
            media = cl.photo_upload(self.location_file_post,
                                        caption =caption)
            print("Mensaje de la mañana publicado")
        # Lunch 11 < time.hour <  13
        elif time.hour > AFTERNOON[0] and time.hour < AFTERNOON[1]:
            caption = "Nada mejor que una buena receta novedosa para el almuerzo. Recuerde que Carnes Ibarra tiene diferente cortes de carnes y charcuteria" + caption 
            media = cl.photo_upload(path=self.location_file_post,
                            caption=caption)
            print("Mensaje del medio dia publicado")
        # Evening 18  < time.hour < 20
        elif time.hour > EVENING[0] and time.hour < EVENING[1]:
            caption = "Luego de una buena cena con Carnes Ibarra, una nueva palabra" + caption 
            media = cl.photo_upload(path=self.location_file_post,
                            caption=caption)
            print("Mensaje de la tarde publicado")
