from gpiozero import Button
from signal import pause

import sys
import Adafruit_DHT
import time
import os

os.environ['TZ'] = 'US/Central'
time.tzset()

def test_started():
    print("test started")

def test_completed():
    print("test completed")

def test_function():
    humidity, temperature = Adafruit_DHT.read_retry(11,5)
    if temperature is None:
        print(time.strftime('%Y-%m-%d %H:%M:%S')+'     TEMP READ ERROR     '+str(laser.active_time/3600))
        f = open("/home/pi/testlog.txt","a+")
        f.write(time.strftime('%Y-%m-%d %H:%M:%S')+'     TEMP READ ERROR     '+str(laser.active_time/3600)+'\n')
        f.close()
    else:
        print(time.strftime('%Y-%m-%d %H:%M:%S')+'     {:.1f} F'.format(temperature*9/5+32)+'    '+str(temperature)+' C'+'    '+str(laser.active_time/3600))
        f = open("/home/pi/testlog.txt","a+")
        f.write(time.strftime('%Y-%m-%d %H:%M:%S')+'     {:.1f} F'.format(temperature*9/5+32)+'    '+str(temperature)+' C'+'    '+str(laser.active_time/3600)+'\n')
        f.close()

laser = Button(4,bounce_time=0,pull_up=True,hold_repeat=True)
laser.when_pressed = test_started
laser.when_held = test_function
laser.when_released = test_completed

pause()
