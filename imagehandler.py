import os
import random


def choose_image(bot_response):
   if bot_response.split('.', maxsplit=1)[0] == "#image":
      image_name = bot_response.split(' ', maxsplit=1)[0].split('.', maxsplit=1)[1].replace('.', '/')
      image_url = "./static/images/" + image_name + '/'
      while os.path.isdir(image_url):
         image_url = image_url + random.choice(os.listdir(image_url)) + '/'
      return image_url, bot_response.split(' ', maxsplit=1)[1]
   else:
      return None, bot_response
