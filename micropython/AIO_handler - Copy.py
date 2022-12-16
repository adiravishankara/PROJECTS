import network
#from secrets import *
import time
import urequests as requests
from lib.umqtt.robust import MQTTClient
import os
import sys
import uasyncio as asyncio
from machine import Pin




class AIO_handler:
    def __init__(self):
        self.WLAN_SSID = 'HUMAX-97E53'
        self.WLAN_PWD = 'MjFJLTdkNWM5N'
        self.AIO_UNAME = 'adiravishankara'
        self.AIO_KEY = 'aio_VjMw16CXuLa9mgL2j2Fz7ZlcIAF8'

        self.system_state = 0

        # Setting up the control pin just type in the number of the pin you connected
        self.set_pin(7)

        # Setting up wifi. You need to make sure the proper credentials are in secrets.py
        self.connect_to_wifi()

        # This will make a listener
        self.start_client()
        asyncio.run(self.run_async())



    def run_async(self):
        self.button_task = asyncio.create_task(self.button_interrupt())
        await asyncio.gather(self.button_task)

    def set_pin(self, pin):
        self.control_pin = machine.Pin(pin, Pin.OUT)
        self.control_pin.low()

    def connect_to_wifi(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        try:
            wlan.connect(self.WLAN_SSID, self.WLAN_PWD)
            while not wlan.isconnected:
                print('Waiting for a Connection')
                time.sleep(0.5)
            print('Connected!')
        except Exception as e:
            print("Something went wrong")
            print(type(e).__name__, e)
            sys.exit()

    def start_client(self):
        random_num = int.from_bytes(os.urandom(3), 'little')
        mqtt_client_id = bytes('client_' + str(random_num), 'utf-8')

        self.AIO_URL = b'io.adafruit.com'
        #ADAFRUIT_USERNAME = b'adiravishankara'
        #ADAFRUIT_IO_KEY = b'aio_VjMw16CXuLa9mgL2j2Fz7ZlcIAF8'
        self.AIO_FEED = b'hydroponics.switch'

        self.client = MQTTClient(client_id=mqtt_client_id, server=self.AIO_URL, user=self.AIO_UNAME, password=self.AIO_KEY, ssl=False)

        try:
            self.client.connect()
        except Exception as e:
            print("Error with MQTT Server")
            print(type(e).__name__, e)
            sys.exit()

        self.feed = bytes('{:s}/feeds/{:s}'.format(self.AIO_UNAME, self.AIO_FEED), 'utf-8')
        self.client.set_callback(self.switch_callback)
        self.client.subscribe(self.feed)
        print("System is functional!")

    async def button_interrupt(self):
        while True:
            try:
                self.client.wait_msg()
            except KeyboardInterrupt:
                print("Ctrl-C pressed, exiting now!")
                sys.exit()
            await asyncio.sleep(0)

    def switch_callback(self, topic, msg):
        if self.system_state == 0:
            self.system_state = 1
            self.control_pin.high()
            print("\nSwitching System On")

        else:
            self.system_state = 0
            self.control_pin.low
            print("\nSwitching System Off")

        print('topic: {}\nmsg: {}'.format(topic, msg))







if __name__ == '__main__':
    A = AIO_handler()

