import time
import winsound
from plyer import notification

def notify():
    notification.notify(
        title='ANTI CHEAT ENABLED',
        message='Nothing to see here...',
        timeout=8  
    )


    winsound.Beep(1000, 750)  

if __name__ == "__main__":
    notify()
    time.sleep(2) 
