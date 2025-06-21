import network
import json
import time
import random
import gc
import machine
import umqttsimple
import ubinascii
import _thread # LA libreria obliga a preguntar

class MQTTSender:
    
    def __init__(self, settings = ""):
        self.settings = settings
        self.topic_sub = self.settings["topic_sub"]
        self.topic_pub = self.settings["topic_pub"]
        self.client_id = ubinascii.hexlify(machine.unique_id())
        self.client = umqttsimple.MQTTClient(self.client_id,
                                             self.settings["broker"],
                                             self.settings["port"])
        self.client.set_callback(self.information_recieved)
        self.client.connect()
        print("[INFO] Broker connected")
        self.client.subscribe(self.settings["topic_sub"])
        _thread.start_new_thread(self.download, ())
        
    def download(self):
        while True:
            self.client.check_msg()
            time.sleep(0.1)
        
    def information_recieved(self, topic, message):
        print(f"[INFO] Topic {topic}")
        print(f"[INFO] Message {message}")


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
    mqtt_sensor = MQTTSender(settings)
    while True:
        mqtt_sensor.client.publish(settings["topic_pub"], "Me llamo felipe")
        time.sleep(1)
