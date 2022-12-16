import machine
import network
from umqtt.simple import MQTTClient
import time
from wifi_handler import connect_to_wifi
import secrets


class AWS_IOT_HANDLER:
    def __init__(self):
        self.setup_wifi()
        self.setup_aws()

    def setup_wifi(self):
        self.wlan = connect_to_wifi(secrets.secrets['wlan_ssid'], secrets.secrets['wlan_pwd'])

    def setup_aws(self):
        self.mqtt_broker = MQTTClient(secrets.secrets['aws_client_id'],
                                      secrets.secrets['aws_endpoint'],
                                      port=8893,
                                      keepalive=10000,
                                      ssl=True,
                                      ssl_params=self.wlan.get_ssl_params())


    def read_pem_file(self, file):
        with open(file, 'r') as f:
            _ = f.read().strip()
            split_text = _.split('\n')
            base64_text = ''.join(split_text[1:-1])

        return ubinascii.a2b_base64(base64_text)
        
    



if __name__ == "__main__":
    AWS_IOT_HANDLER()
    print('All is well')
