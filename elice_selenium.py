from selenium import webdriver as wb
from selenium.webdriver.common.by import By
import time
import json

def selenium_start(
    selectors,
    json_file_path = r'c:\keys\idpw입력.json',
    email_key = 'email',
    password_key = 'password',
    site_path = 'https://2023-gj-aischool.elice.io/my'
):
    print('*************Attendence Start!!*************')

    print(json_file_path) 

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    email, password = data.get(email_key), data.get(password_key)

    driver = wb.Chrome()
    driver.get(site_path)

    time.sleep(5)
    email_box = driver.find_element(By.CSS_SELECTOR, selectors['email_box_selector'])
    password_box = driver.find_element(By.CSS_SELECTOR, selectors['password_box_selector'])
    login_button = driver.find_element(By.CSS_SELECTOR, selectors['login_button_selector'])

    email_box.send_keys(email)
    time.sleep(2)
    password_box.send_keys(password)
    time.sleep(2)
    login_button.click()

    time.sleep(5)

    attendance_button = driver.find_element(By.CSS_SELECTOR, selectors['attendance_button_selector'])
    print(attendance_button)
    attendance_button.click()

    time.sleep(5)

    print('*************Attendence Completed!*************')


if __name__ == '__main__':
    selectors = {
        'email_box_selector' : '#root > div > main > div > div > div.css-pw7jst.e5d9byx0 > form > div.MuiFormControl-root.MuiFormControl-fullWidth.MuiTextField-root.css-uyinme > div > input',
        'password_box_selector' : '#root > div > main > div > div > div.css-pw7jst.e5d9byx0 > form > div.MuiStack-root.css-tgpajw > div > div > input',
        'login_button_selector' : '#root > div > main > div > div > div.css-pw7jst.e5d9byx0 > form > button',
        'attendance_button_selector' : '#root > main > div > div > div.MuiStack-root.css-1ssmg91 > section:nth-child(2) > div.MuiCardContent-root.css-17ixjzr > div > div.MuiStack-root.css-p27s4m > button'
    }
    
    selenium_start(selectors)




