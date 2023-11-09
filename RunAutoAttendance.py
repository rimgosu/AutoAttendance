from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json
import sched
import time
from datetime import datetime, timedelta
import pystray
import PIL.Image
import threading


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

    try:
        attendance_button = driver.find_element(By.XPATH, "//button[contains(text(),'출석')]")
    except:
        attendance_button = driver.find_element(By.XPATH, "//button[contains(text(),'퇴실')]")

    print(f"attendence_button : {attendance_button.text}")
    attendance_button.click()

    time.sleep(5)

    print('*************Attendence Completed!*************')

def elice_schedule(
    selectors,
    hour = 8,
    minute = 51,
    second = 0
):
    while True:
        # 스케줄러 생성
        scheduler = sched.scheduler(time.time, time.sleep)

        # 원하는 실행 시간 계산
        now = datetime.now()
        target_time = now.replace(hour=hour, minute=minute, second=second, microsecond=0)

        # 만약 현재 시간이 목표 시간보다 크면 다음 날로 설정
        if now > target_time:
            target_time += timedelta(days=1)

        # 목표 시간까지 대기
        time_difference = (target_time - now).total_seconds()
        time.sleep(time_difference)

        # 함수를 스케줄에 추가하여 실행
        scheduler.enter(0, 1, selenium_start, (selectors,))
        scheduler.run()

class EliceCheck:
    def __init__(self):
        self.image = PIL.Image.open('./data/icon.png')
        self.icon = pystray.Icon('EliceCheck', self.image, menu=self.create_menu())
        self.selectors = {
            'email_box_selector' : '#root > div > main > div > div > div.css-pw7jst.e5d9byx0 > form > div.MuiFormControl-root.MuiFormControl-fullWidth.MuiTextField-root.css-uyinme > div > input',
            'password_box_selector' : '#root > div > main > div > div > div.css-pw7jst.e5d9byx0 > form > div.MuiStack-root.css-tgpajw > div > div > input',
            'login_button_selector' : '#root > div > main > div > div > div.css-pw7jst.e5d9byx0 > form > button',
            'attendance_button_selector' : '#root > main > div > div > div.MuiStack-root.css-1ssmg91 > section:nth-child(2) > div.MuiCardContent-root.css-17ixjzr > div > div.MuiStack-root.css-p27s4m > button'
        }
        
        

    def create_menu(self):
        return pystray.Menu(pystray.MenuItem("Exit", self.on_clicked))

    def on_clicked(self, icon, item):
        icon.stop()

    def run_icon(self):
        self.icon.run()

    def run_schedule(self, hour, minute, second):
        elice_schedule(
            self.selectors,
            hour=hour,
            minute=minute,
            second=second
        )

    def start(self, times):
        icon_thread = threading.Thread(target=self.run_icon)
        icon_thread.daemon = True
        icon_thread.start()

        schedule_thread = threading.Thread(target=self.run_schedule, args=times['attendance_time'])
        schedule_thread.daemon = True
        schedule_thread.start()

        schedule_thread2 = threading.Thread(target=self.run_schedule, args=times['checkout_time'])
        schedule_thread2.daemon = True
        schedule_thread2.start()

        icon_thread.join()

if __name__ == "__main__":
    times = {
        'attendance_time' : (8, 51, 0), # 8시 51분
        'checkout_time' : (17, 51, 0) # 17시 51분
    }

    print("*************AutoAttendence is running...*************")

    elice_checker = EliceCheck()
    elice_checker.start(times)
