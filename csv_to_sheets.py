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

#Create the color palette (for this palette it was used this page: https://coolors.co/)
my_palette = ["#2E86AB", "#A23B72", "#40B9EC", "#D64D96", "#3B1F2B"]

#Function to create charts and export them to a PDF
def charts_to_pdf(df, columns, pdf_path):
    #Unique value threshold to avoid overly detailed charts
    HIGHER_UNIQUE_VALUE = 24
    
    #Format to ensure all charts have the same font type and size.
    titles = 20
    label = 12
    font = 'Tahoma'
    name = 10

    #Create a specific chart with two variables
    with PdfPages(pdf_path) as pdf:
        author_counts = df.groupby('Readers Choice Category')['Author'].nunique().sort_values(ascending=False)
        
        plt.figure(figsize=(14, 8))
        sns.barplot(x=author_counts.index, y=author_counts.values, palette=my_palette)
        plt.title('AUTHORS BY CATEGORY', fontsize=titles, fontweight='bold', fontname=font)
        plt.xlabel('Category', fontsize=label, fontname=font)
        plt.ylabel('Number of Authors', fontsize=label, fontname=font)
        plt.xticks(rotation=30, ha='right', fontsize=label, fontname=font)
        
        # Add values above the bars
        for index, value in enumerate(author_counts.values):
            plt.text(index, value + 0.1, str(value), ha='center', va='bottom', fontsize=name, fontname=font)
        
        pdf.savefig()  # Save the current figure to the PDF file
        plt.tight_layout()  # Automatically adjust elements to avoid overlap
        plt.close()  # Close the figure to prevent overwriting

        #Create charts with the variable "HIGHER_UNIQUE_VALUE"
        for column in columns:
            header = df[column]
            header_counts = header.value_counts()
            
            # Sort values by count (descending)
            header_counts_sorted = header_counts.sort_values(ascending=False)

            # Check the number of unique values
            unique_value = header_counts.count()
            
            if unique_value <= HIGHER_UNIQUE_VALUE:
                plt.figure(figsize=(14, 8))
                ax = sns.barplot(x=header_counts_sorted.index, y=header_counts_sorted.values, palette=my_palette, order=header_counts_sorted.index)
                plt.title(column.upper(), fontsize=titles, fontweight='bold', fontname=font)
                plt.xlabel('Categories', fontsize=label, fontname=font)
                plt.ylabel('Quantity', fontsize=label, fontname=font)
                plt.xticks(rotation=30, ha='right', fontsize=label, fontname=font)
                
                # Add values above the bars
                for index, value in enumerate(header_counts.values):
                    plt.text(index, value + 0.1, str(value), ha='center', va='bottom', fontsize=name, fontname=font)
                
                pdf.savefig()  # Save the current figure to the PDF file
                plt.tight_layout()  # Automatically adjust elements to avoid overlap
                plt.close()  # Close the figure to prevent overwriting