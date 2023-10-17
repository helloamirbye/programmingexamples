import datetime

def Delay():
    t1 = datetime.datetime.now()
    while True:
        t2 = datetime.datetime.now()
        if t2.second != t1.second:
            break
        
def Timer():
    try:
        seconds=input("Please Set Timer(hour:minute:second exp=> 0:28:17)=> ")
        seconds = seconds.split(":")
        second = int(seconds[2])
        minute = int(seconds[1])
        hour = int(seconds[0])
    except:
        print("Error!")
        Timer()
        return

    if (second >=60 or second < 0) or (minute >=60 or minute < 0) or (hour >=24 or hour < 0) :
        print("Error!")
        Timer()
        return

    for h in range(hour,-1,-1):
        for m in range(minute,-1,-1):
            for s in range(second,-1,-1):
                print("\rRemaining Time=> {:02}:{:02}:{:02}".format(h,m,s),end="")
                Delay()
            second = 59
    print("\nIt's Done.")

Timer()