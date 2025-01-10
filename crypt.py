

import os , sys , ctypes


def log(message):
    print(message)

def clear():
    if platform.system() == "Windows":
        os.system("cls")  
    else:
        os.system("clear")  
