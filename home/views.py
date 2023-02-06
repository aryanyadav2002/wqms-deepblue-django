from django.shortcuts import render,HttpResponse

from googleapiclient.discovery import build
from google.oauth2 import service_account

# import json
# data=open('./static/keys.json').read()
# dict_data=json.loads(data)
# # str_data=json.dumps(dict_data)
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# SCOPES = ['https://www.googleapis.com/auth/sqlservice.admin']
# SERVICE_ACCOUNT_FILE = 'keys.json'
creds=None
creds = service_account.Credentials.from_service_account_file(
        './static/keys.json', scopes=SCOPES)
SAMPLE_SPREADSHEET_ID = '15YjGKgbatmC6J8ZK2jLYnFXTd0gztKACUlaTRCP5C8E'
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Sheet1").execute()
values = result.get('values', [])
for item in reversed(values):
    latest=item
    print(latest)
    break

temp=30
ph=7
turb=550
tds=60
show={
    'temp': latest[2],
    'ph':latest[3],
    'turb':latest[4],
    'tds':latest[5],
}


# Create your views here.
def index(request):
    return render(request,'homepage.html')


def getreadings(request):
    
    return render(request,'readings.html',{'show':show})