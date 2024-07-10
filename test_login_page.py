# # # import pytest
# # # import openpyxl
# # # # from test_data.xlsx import test_data
# # # from Orange_login_page import OrangeHRMLoginPage
# # #
# # # from selenium import webdriver
# # # from selenium.webdriver.common.by import By
# # # from selenium.webdriver.chrome.service import Service as ChromeService
# # # from selenium.webdriver.support.ui import WebDriverWait
# # # from selenium.webdriver.support import expected_conditions as EC
# # # from datetime import datetime
# # # import os
# # #
# # #
# # # file_path = os.path.abspath("testdata.xlsx")
# # #
# # # def read_excel(file_path):
# # #     wb = openpyxl.load_workbook(file_path)
# # #     ws = wb.active
# # #     data = []
# # #     for row in ws.iter_rows(min_row=2, values_only=True):
# # #         if len(row) < 7:
# # #             row = tuple(list(row) + [None] * (7 - len(row)))  # Pad the row with None to ensure it has 7 elements
# # #         data.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
# # #     return data, wb, ws
# # #
# # # def write_result(ws, row, result):
# # #     ws.cell(row=row, column=7, value=result)
# # #     now = datetime.now()
# # #     ws.cell(row=row, column=4, value=now.date())
# # #     ws.cell(row=row, column=5, value=now.time())
# # #
# # # @pytest.fixture
# # # def browser():
# # #     # Update this path to the actual location of your ChromeDriver executable
# # #     chrome_service = ChromeService(r"C:\path\to\your\chromedriver.exe")
# # #     driver = webdriver.Chrome(service=chrome_service)
# # #     driver.maximize_window()
# # #     yield driver
# # #     driver.quit()
# # #
# # # # Read data from Excel and ensure it includes all 7 columns
# # # test_data, workbook, worksheet = read_excel(file_path)
# # #
# # # @pytest.mark.parametrize("test_id, username, password, date, time, tester, result", test_data)
# # # def test_orangehrm_login(browser, test_id, username, password, date, time, tester, result):
# # #     login_page = OrangeHRMLoginPage(browser)
# # #     login_page.navigate_to_login_page()
# # #
# # #     try:
# # #         login_page.login(username, password)
# # #
# # #         # Wait for login success (customize as per your application)
# # #         WebDriverWait(browser, 10).until(
# # #             EC.visibility_of_element_located((By.ID, "dashboard-quick-launch-panel-menu_holder"))
# # #         )
# # #         test_result = "Passed"
# # #     except Exception as e:
# # #         print(f"Error during login: {e}")
# # #         test_result = "Failed"
# # #
# # #     # Write the result back to the Excel file
# # #     write_result(worksheet, test_id + 1, test_result)
# # #     workbook.save(file_path)
# # #
# # # if __name__ == "__main__":
# # #     pytest.main(["-v", __file__])
# # #
# # #
# # import pytest
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from openpyxl import load_workbook
# # import datetime
# #
# #
# # def read_excel(file_path):
# #     wb = load_workbook(file_path)
# #     ws = wb.active
# #     data = []
# #     for row in ws.iter_rows(min_row=2, values_only=True):
# #         data.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
# #     return data, wb, ws
# #
# #
# # @pytest.fixture
# # def browser():
# #     driver = webdriver.Chrome()
# #     yield driver
# #     driver.quit()
# #
# #
# # @pytest.mark.parametrize("test_id, username, password, date, time, tester, result", [
# #     ('1', 'Admin', 'admin123', datetime.datetime(2024, 6, 6), datetime.time(12, 0), 'TesterName', None),
# #     ('2', 'invalid', 'incorrect', datetime.datetime(2024, 6, 7), datetime.time(12, 30), 'TesterName', None),
# #     # Add more test cases as needed
# # ])
# # def test_login(browser, test_id, username, password, date, time, tester, result):
# #     url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
# #     browser.get(url)
# #
# #     # Perform login steps
# #     WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(username)
# #     WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys(password)
# #     WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
# #
# #     try:
# #         WebDriverWait(browser, 10).until(
# #             EC.visibility_of_element_located((By.XPATH, "//p[text()='Invalid credentials']")))
# #         result = "Fail"
# #     except:
# #         result = "Pass"
# #
# #     # Write result back to Excel
# #     test_data, workbook, worksheet = read_excel(
# #         r"C:\Users\HP\Pytest projects sample excelfile orange DDF\pythonProject\OrangeDDF\testdata.xlsx")
# #     for row in worksheet.iter_rows(min_row=2):
# #         if row[0].value == test_id:
# #             row[6].value = result
# #             break
# #     workbook.save(r"C:\Users\HP\Pytest projects sample excelfile orange DDF\pythonProject\OrangeDDF\testdata.xlsx")
# #
# #
# # if __name__ == "__main__":
# #     pytest.main(["-v", "test_login_page.py"])
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from openpyxl import load_workbook
# import datetime
#
#
# def read_excel(file_path):
#     wb = load_workbook(file_path)
#     ws = wb.active
#     data = []
#     for row in ws.iter_rows(min_row=2, values_only=True):
#         data.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
#     return data, wb, ws
#
#
# @pytest.fixture
# def browser():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()
#
#
# @pytest.mark.parametrize("test_id, username, password, date, time, tester, result", [
#     ('1', 'Admin', 'admin123', datetime.datetime(2024, 6, 6), datetime.time(12, 0), 'TesterName', None),
#     ('2', 'invalid', 'incorrect', datetime.datetime(2024, 6, 7), datetime.time(12, 30), 'TesterName', None),
#     # Add more test cases as needed
# ])
# def test_login(browser, test_id, username, password, date, time, tester, result):
#     url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
#     browser.get(url)
#
#     # Perform login steps
#     # WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.))).send_keys(username)
#     # WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys(password)
#     # WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
#
#     try:
#         WebDriverWait(browser, 10).until(
#             EC.visibility_of_element_located((By.XPATH, "//p[text()='Invalid credentials']")))
#         result = "Fail"
#     except:
#         result = "Pass"
#
#     # Write result back to Excel
#     test_data, workbook, worksheet = read_excel(
#         r"C:\Users\HP\Pytest projects sample excelfile orange DDF\pythonProject\OrangeDDF\testdata.xlsx")
#     for row in worksheet.iter_rows(min_row=2):
#         if row[0].value == test_id:
#             row[6].value = result
#             break
#     workbook.save(r"C:\Users\HP\Pytest projects sample excelfile orange DDF\pythonProject\OrangeDDF\testdata.xlsx")
#
#
# if __name__ == "__main__":
#     pytest.main(["-v", "test_login_page.py"])


import pytest
from selenium import webdriver
from pages.excel_utils import write_to_excel
from pages.Orange_login_page import LoginPage


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.parametrize("test_id, username, password, tester_name", [
    (1, "Admin", "admin123", "Tester1"),
    (2, "Admin", "admin12345", "Tester2"),
    (3, "Admin", "admin123", "Tester3"),
    (4, "Admin", "admin12345", "Tester4"),
    (5, "Admin", "admin123", "Tester5")
])
def test_login(setup, test_id, username, password, tester_name):
    login_page = LoginPage(setup)
    login_page.login(username, password)

    if login_page.is_login_successful():
        test_result = "Passed"
    else:
        test_result = "Failed"

    # Get current date and time (you can use datetime module for this)
    date = "2024-07-10"  # Replace with actual date
    time = "10:00 AM"  # Replace with actual time

    data = [test_id, username, password, date, time, tester_name, test_result]
    write_to_excel("testdata.xlsx", data)
