import json

with open('./static/info.json', 'r') as file:
   info_list = json.load(file)


def update_info(message):
   if message.find('#Info.'):
      message = message.split('#')
      for i in info_list:
         for j in range(message.count('Info.'+i)):
            message[message.index('Info.'+i)] = info_list[i]
      return ''.join(message)
   else:
      return message

