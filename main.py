import openpyxl
from datetime import datetime

# Create a new workbook and add a worksheet
wb = openpyxl.Workbook()
ws = wb.active

# Add current time to a cell
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
ws['A1'] = current_time

# Define the path to save the workbook
unc_path = r"test.xlsx"

# Save the workbook
try:
    wb.save(unc_path)
    print("Workbook saved successfully.")
except PermissionError as e:
    print(f"PermissionError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
