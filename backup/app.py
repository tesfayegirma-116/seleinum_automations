import requests
import json

url = "https://api.telegram.org/bot5692464682:AAEKqvCKMsOKk2Po9m-dQP4_koR3OqumDjc/getUpdates?offset=-1"

links = requests.get(url)

data = json.loads(links.text)


for i in data['result']:
    try:
        if 'edited_message' in i:
            link = i['edited_message']['text']
        else:
            link = i['message']['text']
    except:
        print("no links found")

print(link)
