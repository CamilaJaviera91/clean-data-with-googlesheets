#Add libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from matplotlib.backends.backend_pdf import PdfPages
import math

#Add libraries from google_sheets_utils
from google_sheets_utils import sheets_to_dataframe as sd
from google_sheets_utils import csv_to_sheets as cs

#Add warnings and plt style
warnings.filterwarnings('ignore')
plt.style.use("default")

#Obtain data frame from google_sheets_extractor
df = sd()

#Columns to be removed
columns_to_remove = ['source_URL', 'Book Description', 'About the Author', 'Kindle Version and Price', 'Readers Choice Votes']

#Remove the columns
df.drop(columns=columns_to_remove, inplace=True)

#Convert the date column to datetime type
df['First Published date'] = pd.to_datetime(df['First Published date'], errors='coerce')

months = df['First Published date'].dt.month
years = df['First Published date'].dt.year

#Extract only the year and month
df['Published Year'] = years.convert_dtypes(convert_floating=False)
df['Published Month'] = months.convert_dtypes(convert_floating=False)

#Remove the original date column
df.drop(columns=['First Published date'], inplace=True)

#Current folder
folder = './'

#Save the modified .CSV file
output_file_path = folder + 'books_clean.csv'
df.to_csv(output_file_path, index=False)

#Read the new .CSV file
file_path = folder + 'books_clean.csv'
df = pd.read_csv(file_path)

#Save the .csv file to Google Sheets
cs()