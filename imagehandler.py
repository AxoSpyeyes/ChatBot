import os
import random


def choose_image(bot_response):
   if bot_response.split('.', maxsplit=1)[0] == "#image" and bot_response.split('.', maxsplit=2)[1] == "furniture":
      image_type = bot_response.split(' ', maxsplit=1)[0].split('.')[2]
      if image_type == "furniture":
         image_url = "./static/images/furniture"
         image_type = random.choice(os.listdir(image_url))
      image_url = "./static/images/furniture/" + image_type + "/"
      return image_url + random.choice(os.listdir(image_url)), bot_response.split(' ', maxsplit=1)[1]

   else:
      return None, bot_response
