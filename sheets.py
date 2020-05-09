import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]         

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
                                  
client = gspread.authorize(creds)

sheet = client.open("spreaddemo").sheet1

data = sheet.get_all_records()
#pprint(data)

row = sheet.row_values(3)  # Get a specific row
col = sheet.col_values(3)  # Get a specific column
#cell = sheet.cell(2,1).value  # Get the value of a specific cell
now = sheet.row_values(4)
now = list(map(int, now)) 
print (now)
print(now.index(75))