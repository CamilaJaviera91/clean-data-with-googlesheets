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
