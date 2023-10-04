import sched
import time
from datetime import datetime, timedelta
from elice_selenium import selenium_start

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


if __name__ == '__main__':

    selectors = {
        'email_box_selector' : '#root > div > main > div > div > div.css-pw7jst.e5d9byx0 > form > div.MuiFormControl-root.MuiFormControl-fullWidth.MuiTextField-root.css-uyinme > div > input',
        'password_box_selector' : '#root > div > main > div > div > div.css-pw7jst.e5d9byx0 > form > div.MuiStack-root.css-tgpajw > div > div > input',
        'login_button_selector' : '#root > div > main > div > div > div.css-pw7jst.e5d9byx0 > form > button',
        'attendance_button_selector' : '#root > main > div > div > div.MuiStack-root.css-1ssmg91 > section:nth-child(2) > div.MuiCardContent-root.css-17ixjzr > div > div.MuiStack-root.css-p27s4m > button'
    }

    elice_schedule(
        selectors,
        hour = 0,
        minute = 13,
        second = 30
    )
