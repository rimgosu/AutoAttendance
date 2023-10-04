import pystray
import PIL.Image
import threading
from elice_schdule import elice_schedule

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
        'attendance_time' : (8, 51, 0),
        'checkout_time' : (17, 51, 0)
    }

    elice_checker = EliceCheck()
    elice_checker.start(times)
