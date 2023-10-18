# pip install colorama
# # or
# conda install -c anaconda colorama

import time,os
from colorama import Fore

def Timer():
    os.system("cls")
    print("Please Set Seconds: ",end="")
    seconds=input()

    while not seconds.isdigit():
        os.system("cls")
        print("That wasn't an integer! Please enter an integer for Set Seconds: ",end="")
        seconds=input()

    seconds=int(seconds)
    second = 0
    minute = 0
    hour = 0
    if seconds < 60:
        second = seconds       
    elif seconds >= 60:
        minute = seconds // 60
        second = seconds % 60
        if minute >= 60:
            hour = minute // 60
            minute += (minute % 60)   

    os.system("cls")
    for h in range(hour,-1,-1):
        for m in range(minute,-1,-1):
            for s in range(second,-1,-1):
                if h==0 and m==0 and s<11:
                    print(Fore.RED+"\rRemaing Time=> {:02}:{:02}:{:02}".format(h,m,s),end="")
                    if s!=0:
                        time.sleep(1)
                else:
                    print("\rRemaing Time=> {:02}:{:02}:{:02}".format(h,m,s),end="")
                    time.sleep(1)
            second = 59
    print("\n\n\n\t\t\t-----[[[ EXPLOSION !!! ]]]-----\n\n\n"+Fore.RESET)
    
Timer()