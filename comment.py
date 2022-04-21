import openpyxl
from social_network import social_media

workbook = openpyxl.load_workbook(filename="acc.xlsx")
sheet = workbook.active
username = sheet['A2'].value
password = sheet['B2'].value

login = social_media(username, password)
login.comment_post()
