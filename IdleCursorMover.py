import datetime
import time
import pyautogui as pg
moveIntr=int(input("Movement Interval (Seconds): "))

while True:
    pg.moveTo(100.0,100.0,0)
    pg.moveTo(100.0,200.0,0.5)
    pg.moveTo(200.0,200.0,0.5)
    pg.moveTo(200.0,100.0,0.5)
    pg.moveTo(100.0,100.0,0.5)
    print("Next Movement At "+str(datetime.datetime.now()+datetime.timedelta(seconds=moveIntr-2)))
    time.sleep(moveIntr-2)