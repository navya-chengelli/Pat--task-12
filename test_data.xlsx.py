import openpyxl
from openpyxl import Workbook
from datetime import datetime

# Create a workbook and select the active worksheet
wb = Workbook()
ws = wb.active

# Define the headers
headers = ["Test ID", "Username", "Password", "Date", "Time of Test", "Name of Tester", "Test Result"]
ws.append(headers)

# Add test data (for demonstration, we'll add 5 sets of credentials)
test_data = [
    [1, "Admin", "admin123", "", "", "Tester1", ""],
    [2, "testuser1", "password1", "", "", "Tester1", ""],
    [3, "testuser2", "password2", "", "", "Tester1", ""],
    [4, "testuser3", "password3", "", "", "Tester1", ""],
    [5, "testuser4", "password4", "", "", "Tester1", ""]
]

for data in test_data:
    ws.append(data)

# Save the workbook
wb.save("test_data.xlsx")
