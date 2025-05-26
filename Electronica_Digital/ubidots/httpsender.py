import network
import json
import time
import random
import requests
import gc

class HTTPSender:
    def __init__(self, host="", token="", device_label="", variable_label=""):
        self.host = host
        self.token = token
        self.device_label = device_label
        self.variable_label = variable_label
        self.payload = ""
        
    def post(self):
        endpoint = f"https://{self.host}/api/v1.6/devices/{self.device_label}/"
        print(f"[INFO] Endpoint: {endpoint}")
        headers = {"X-Auth-Token" : self.token,
                   "Content-Type" : "application/json"}
        temperature = 100*random.random()
        self.payload = {"temperature" : temperature}
        request = requests.post(url = endpoint,
                                headers = headers,
                                json = self.payload)
        print(f"[POST INFO] {request.status_code}")

def load_settings():
    #settings.json está guardado en el microcontrolador
    with open("settings.json", "r") as f:
        settings = json.loads(f.read())
    print(f"[INFO] Settings: {settings}")
    return settings

def connect_wifi(settings):
    wlan = network.WLAN(network.WLAN.IF_STA)
    wlan.active(True)
    wlan.connect(settings["ssid"], settings["password"])
    while not wlan.isconnected():
        print(f"[INFO] Connecting to: {settings["ssid"]}")
        time.sleep(1)
    print(f"[INFO] WLAN connected to: {settings["ssid"]}")
    
    
if __name__ == "__main__":
    settings = load_settings()
    connect_wifi(settings)
    http_sensor = HTTPSender(settings["host"],settings["token"], settings["device_label"], settings["variable_label"])
    while True:
        http_sensor.post()
        gc.collect()
        time.sleep(1)
        
"""
print(wlan.scan())
"""