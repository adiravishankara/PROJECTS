# Imports

import machine
import network
import ssl
import time
import ubinascii
from machine import Pin, Timer
import ntptime
from umqtt.simple import MQTTClient
import sys
from secrets import secrets
import uasyncio as asyncio

class AWS_HANDLER:
    def __init__(self):
        self.wlan = self.connect_to_wifi(secrets['wlan_ssid'], secrets['wlan_pwd'])
        ntptime.settime()
        self.create_mqtt_client()
        # while True:
        #     self.message_checker()
        asyncio.run(self.async_system())


    def connect_to_wifi(self, SSID, PWD):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        led = Pin("LED", Pin.OUT)
        try:
            wlan.connect(SSID, PWD)
            while not wlan.isconnected:
                # print('Waiting for a Connection')
                led.on()
                asyncio.sleep_ms(500)
                led.off()
            print("Wifi Connected!")
        except Exception as e:
            print("Something went wrong")
            print(type(e).__name__, e)
            sys.exit()

        return wlan

    def create_mqtt_client(self):
        print('Connecting to MQTT Client')
        # MQTT client and broker constants
        MQTT_CLIENT_KEY = "private.pem.key"
        MQTT_CLIENT_CERT = "certificate.pem.crt"
        MQTT_CLIENT_ID = ubinascii.hexlify(machine.unique_id())

        MQTT_BROKER = secrets['aws_endpoint']
        MQTT_BROKER_CA = "AmazonRootCA1.pem"

        # MQTT topic constants
        MQTT_LED_TOPIC = "picow/led"
        MQTT_BUTTON_TOPIC = "picow/button"

        def read_pem(file):
            with open(file, "r") as input:
                text = input.read().strip()
                split_text = text.split("\n")
                base64_text = "".join(split_text[1:-1])

                return ubinascii.a2b_base64(base64_text)

        key = read_pem(MQTT_CLIENT_KEY)
        cert = read_pem(MQTT_CLIENT_CERT)
        ca = read_pem(MQTT_BROKER_CA)

        self.mqtt_client = MQTTClient(
            MQTT_CLIENT_ID,
            MQTT_BROKER,
            keepalive=60,
            ssl=True,
            ssl_params={
                "key": key,
                "cert": cert,
                "server_hostname": MQTT_BROKER,
                "cert_reqs": ssl.CERT_REQUIRED,
                "cadata": ca,
            },
        )
        self.mqtt_client.connect()
        print('Connected to MQTT Client!\n Setting Up Callbacks')

        self.mqtt_client.set_callback(self.incoming_message_handler)
        print('Callbacks are set')

    def incoming_message_handler(self, topic, msg):
        topic = topic.decode()
        msg = msg.decode()

        print(f'Recieved: {topic} \n {msg}')

    async def message_checker(self):
        while True:
            self.mqtt_client.check_msg()
            await asyncio.sleep(0)

    async def async_system(self):
        self.message_handling_task = asyncio.create_task(self.message_checker())
        await asyncio.gather(self.message_handling_task)


    def publish_message(self, topic, msg):
        self.mqtt_client.publish(topic, msg)



if __name__ == "__main__":
    AWS_HANDLER()