import pystray
import PIL.Image
import threading
from elice_schdule import elice_schedule

image = PIL.Image.open('./data/icon.png')

def on_clicked(icon, item):
    icon.stop()

icon = pystray.Icon('EliceCheck', image, menu=pystray.Menu(
    pystray.MenuItem("Exit", on_clicked)
))

def run_icon(icon):
    icon.run()

def run_schedule(hour, minute, second, selectors):
    elice_schedule(
        selectors,
        hour=hour,
        minute=minute,
        second=second
    )

if __name__ == "__main__":

    selectors = {
        'email_box_selector' : '#root > div > main > div > div > div.css-pw7jst.e5d9byx0 > form > div.MuiFormControl-root.MuiFormControl-fullWidth.MuiTextField-root.css-uyinme > div > input',
        'password_box_selector' : '#root > div > main > div > div > div.css-pw7jst.e5d9byx0 > form > div.MuiStack-root.css-tgpajw > div > div > input',
        'login_button_selector' : '#root > div > main > div > div > div.css-pw7jst.e5d9byx0 > form > button',
        'attendance_button_selector' : '#root > main > div > div > div.MuiStack-root.css-1ssmg91 > section:nth-child(2) > div.MuiCardContent-root.css-17ixjzr > div > div.MuiStack-root.css-p27s4m > button'
    }

    
    icon_thread = threading.Thread(target=run_icon, args=(icon,))
    icon_thread.daemon = True
    icon_thread.start()

    schedule_thread = threading.Thread(target=run_schedule, args=(1, 0, 0, selectors,))
    schedule_thread.daemon = True
    schedule_thread.start()

    schedule_thread2 = threading.Thread(target=run_schedule, args=(1, 0, 30, selectors,))
    schedule_thread2.daemon = True
    schedule_thread2.start()

    icon_thread.join()
