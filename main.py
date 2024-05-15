# main.py

import openpyxl
from datetime import datetime

# Specify the UNC path
unc_path = r'\\spatialfiles.bcgov\sry\Workarea\emillan\!PythonTools\github_test_action\test.xlsx'

# Create a new Excel workbook and select the active sheet
wb = openpyxl.Workbook()
ws = wb.active

# Write the current time in cell A1
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
ws['A1'] = current_time

# Save the workbook
wb.save(unc_path)
