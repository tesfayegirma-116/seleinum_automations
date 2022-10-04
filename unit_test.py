# import requests
# import json
# url = "https://api.telegram.org/bot5692464682:AAEKqvCKMsOKk2Po9m-dQP4_koR3OqumDjc/getUpdates?offset=-1"

# links = requests.get(url)

# data = json.loads(links.text)

# if data['result'][0]:
#     self.link = data['result'][0]['message']['text']
# else:
#     self.link = data['result'][0]['edited_message']['text']

# """
#         Fetch Link From Telegram
#               BOT
#         """
# import requests
# import json
# url = "https://api.telegram.org/bot5692464682:AAEKqvCKMsOKk2Po9m-dQP4_koR3OqumDjc/getUpdates?offset=-1"

# links = requests.get(url)

# data = json.loads(links.text)

# for i in data['result']:
#     try:
#         if 'edited_message' in i:
#             self.link = i['edited_message']['text']
#         else:
#             self.link = i['message']['text']
#     except:
#         print("No links found")
#         exit()
