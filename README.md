# Google Sheets Data Processing and Visualization

This project includes two main scripts: `cvs_to_sheets.py` and `google_sheets_utils.py`. 
<br>
These scripts allow data processing from Google Sheets, performing data cleaning and analysis, and generating charts in a PDF file. Additionally, the processed results can be saved back to Google Sheets.

## Requirements

- Python 3.8+
- Required libraries:
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `google-api-python-client`
  - `google-auth`
  - `google-auth-oauthlib`

Install the dependencies by running:
```bash
pip install -r requirements.txt
```

## Setup

1. **Google API Credentials:**
   - Download the JSON credentials file from the Google Cloud Platform console.
   - Save this file in the project directory with the name `credentials.json`.

2. **Google Spreadsheet ID:**
   - Obtain the spreadsheet ID from the Google Sheets URL.
   - Update the `SPREADSHEET_ID` variable in `google_sheets_utils.py` with this ID.

3. **Data Range:**
   - Ensure the range specified in `RANGE_NAME` (in `google_sheets_utils.py`) matches the data range in your spreadsheet.

## Usage

### Data Extraction, Cleaning, and Analysis

1. **`google_sheets_utils.py`**
   - `sheets_to_dataframe`: Extracts data from Google Sheets and converts it into a pandas DataFrame.
   - `csv_to_sheets`: Saves a CSV file to a Google Spreadsheet.

2. **`cvs_to_sheets.py`**
   - Cleans irrelevant columns and formats the data.
   - Generates charts and exports them as a PDF file.

### Execution

1. **Run the main script:**
   ```bash
   python cvs_to_sheets.py
   ```
   This will perform the following actions:
   - Extract data from Google Sheets.
   - Clean and process the data.
   - Save a cleaned CSV file.
   - Generate charts in a PDF file named `charts_output.pdf`.

2. **Upload the processed file to Google Sheets:**
   - Ensure the generated CSV file (`books_clean.csv`) is in the project folder.
   - Run the `csv_to_sheets` function to upload the file to Google Sheets.

## Output

- **Cleaned CSV file:** `books_clean.csv`
- **PDF file with charts:** `charts_output.pdf`

## Notes

- The color palette for the charts was generated using [Coolors](https://coolors.co/).
- If you encounter issues related to permissions in Google Sheets, verify the credentials and API permissions.

## Project Structure

```plaintext
.
├── cvs_to_sheets.py
├── google_sheets_utils.py
├── credentials.json
├── books_clean.csv
├── charts_output.pdf
├── requirements.txt
└── README.md
```

## Contributions

Contributions are welcome. Please open an issue or submit a pull request if you have improvements or find bugs.