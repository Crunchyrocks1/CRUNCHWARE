import time
import winsound
from plyer import notification
import psutil

def notify():
    notification.notify(
        title='ANTI CHEAT ENABLED',
        message='Nothing to see here...',
        timeout=8  
    )
    winsound.Beep(1000, 750)  

def close_apps():
    processes_to_close = ['notepad.exe', 'cheatengine-x86_64.exe', 'ida.exe']

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'].lower() in processes_to_close:
                proc.terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == "__main__":
    notify()
    close_apps()
    time.sleep(2)
