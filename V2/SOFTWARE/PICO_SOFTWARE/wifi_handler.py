import network
from machine import Pin
import time
import sys


def connect_to_wifi(SSID, PWD):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    led = Pin("LED", Pin.OUT)
    try:
        wlan.connect(SSID, PWD)
        while not wlan.isconnected:
            # print('Waiting for a Connection')
            led.on()
            time.sleep(0.5)
            led.off()
        print("Connected!")
    except Exception as e:
        print("Something went wrong")
        print(type(e).__name__, e)
        sys.exit()

    return wlan


if __name__ == "__main__":
    SSID = "HUMAX-97E53"
    PWD = "MjFJLTdkNWM5N"
    try:
        A = connect_to_wifi(SSID, PWD)
    except Exception as e:
        print(Exception, e)
