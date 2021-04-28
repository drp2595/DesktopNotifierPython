import datetime
from time import sleep
from plyer import notification #for getting notification on your PC

while(True):
    notification.notify(
        title = "Time is"+str(datetime.datetime.now().strftime("%c")), #formated datetim 'Wed Apr 28 11:26:17 2021' <- look like this
        message = "Time To Remind Something",
        timeout  = 20 # the notification stays for 'timeout' sec
    )
    sleep(60*60*12)  # 60 sec * 60 min * 12 hours so 60*60*12.... notification on every 12 hours