import requests
import json
try:
    url = "https://api.telegram.org/bot5692464682:AAEKqvCKMsOKk2Po9m-dQP4_koR3OqumDjc/getUpdates?offset=-1"

    links = requests.get(url)

    getText = links.text

    data = json.loads(getText)

    try:
        link = data['result'][0]['message']['text']
    except:
        pass
    try:
        link = data['result'][0]['edited_message']['text']
    except:
        pass

    print("Try", link)

except:

    with open("./links/link.txt", 'r') as f:
        link = f.readline()
        print(link)
