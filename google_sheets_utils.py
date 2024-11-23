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

#Spreadsheet ID (you can find it in the URL of your Google Sheet example: https://docs.google.com/spreadsheets/d/1aBcD1234EfGhI56789JKLMnOpQrStUvWxYz/edit#gid=0)
#"1aBcD1234EfGhI56789JKLMnOpQrStUvWxYz" this is the id that we need
SPREADSHEET_ID = '1aBcD1234EfGhI56789JKLMnOpQrStUvWxYz'
