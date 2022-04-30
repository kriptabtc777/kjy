import gspread
from oauth2client.service_account import ServiceAccountCredentials 

link = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'] 
creds = ServiceAccountCredentials.from_json_keyfile_name('cred.json', link)
client = gspread.authorize(creds)

sheet = client.open('Курс Валюты').sheet1

get_data = sheet.get_values()

get_data_1 = sheet.cell(2,3).value

# 🇺🇸 USD Розница
usdBuy = sheet.cell(3,2).value
usdSalle = sheet.cell(3,3).value

# 🇪🇺 EUR розница

eurBuy = sheet.cell(4,2).value
eurSalle = sheet.cell(4,3).value

# 🇬🇧 GBP розница

gbpBuy = sheet.cell(5,2).value
gbpSalle = sheet.cell(5,3).value

# 💎 USDT розница

usdtBuy = sheet.cell(3,10).value
usdtSalle = sheet.cell(3,11).value

print(usdtSalle)