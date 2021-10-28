import time
from plyer import notification

if __name__ == '__main__':
    notification.notify(
        title='Pending task:',
        message='You have a task to day today check calender',
        app_icon="D:\Python projects\Reminder\icon2.ico",
        timeout=10

    )
