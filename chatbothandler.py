import requests
import json


def answer(question):
   url = "https://console.dialogflow.com/v1/integrations/messenger/webhook/f044404b-c0a3-4f89-b348-f53f3436bad4/sessions/webdemo-03ae19a0-774e-9dfd-8570-a763ee220744?platform=webdemo"
   payload = {
      "queryInput": {
         "text": {
            "text": question,
            "languageCode": "en"
               }
      }
   }

   headers = {
      'Content-Type': 'application/json'
   }

   response = requests.request("POST", url, headers=headers, json=payload)

   response = response.text.split('\n', maxsplit=1)
   del response[0]
   return json.loads(response[0])['queryResult']['fulfillmentText']