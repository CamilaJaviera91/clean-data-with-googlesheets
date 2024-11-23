#Add libraries
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#Add warnings and plt style
warnings.filterwarnings('ignore')
plt.style.use("default")

#current directory
FOLDER = './'

#spreadsheet ID (you can find it in the URL of your Google Sheet example: https://docs.google.com/spreadsheets/d/1aBcD1234EfGhI56789JKLMnOpQrStUvWxYz/edit#gid=0)
#"1aBcD1234EfGhI56789JKLMnOpQrStUvWxYz" this is the id that we need
SPREADSHEET_ID = '1aBcD1234EfGhI56789JKLMnOpQrStUvWxYz'

#path to the credentials file
#the credentials looks like this:
#{
#   "type": "",
#   "project_id": "",
#   "private_key_id": "",
#   "private_key": "",
#   "client_email": "",
#   "client_id": "",
#   "auth_uri": "",
#   "token_uri": "",
#   "auth_provider_x509_cert_url": "",
#   "client_x509_cert_url": "",
#   "universe_domain": ""
# }
SERVICE_ACCOUNT_FILE = FOLDER + 'credentials.json'

#scopes required to access googlesheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 
          'https://spreadsheets.google.com/feeds', 
          'https://www.googleapis.com/auth/drive.file',
          'https://www.googleapis.com/auth/drive']

#load the credentials from the JSON file
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

#function that transforms the sheets to a dataframe, so it can be work later
def sheets_to_dataframe():

    # Name of the sheet you want to work with
    RANGE_NAME = 'sheets1!A:O'

    # Connect to the Google Sheets API
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    # Read data from the sheet
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])

    data_frame = pd.DataFrame(values)

    try:
        output_file_path = FOLDER + 'google_sheets_books.csv'
        data_frame.to_csv(output_file_path, index=False, columns=None, header=False)
        dfe = pd.read_csv(output_file_path)
        print("Document Saved")  
        
    except NameError as e:
        print(e)

    return dfe

#create a googlesheet from a .csv file
def csv_to_sheets():
    
    # Read the .csv file
    df = pd.read_csv(FOLDER + 'new_name.csv')
    # print(df)
    try:
        service = build('sheets', 'v4', credentials=creds)

        data = [df.columns.tolist()] + df.to_numpy(dtype=str).tolist()
        # Prepare the range where the data will be inserted
        body = {
            'values': data
        }

        # Write data to the spreadsheet
        result = service.spreadsheets().values().update(
            spreadsheetId=SPREADSHEET_ID,
            range='Sheet1!A1',  # Modify this based on where you want to insert the data
            valueInputOption='USER_ENTERED',
            body=body
        ).execute()

        print(f"{result.get('updatedCells')} cells updated.")

    except HttpError as error:
        print(f"An error occurred: {error}")