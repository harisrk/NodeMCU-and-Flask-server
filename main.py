# Complete project details at https://RandomNerdTutorials.com

import time
from umqtt.simple import MQTTClient
import ubinascii
import machine
from machine import Pin
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

led= Pin(14,Pin.OUT)

ssid = 'lg'
password = '12345678'
#mqtt_server = 'REPLACE_WITH_YOUR_MQTT_BROKER_IP'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'

topic_sub = b'state'
topic_pub = b'state'

CONFIG = {
     # Configuration details of the MQTT broker
     "MQTT_BROKER": "192.168.43.126",
     "USER": "",
     "PASSWORD": "",
     "PORT": 1883,
     "TOPIC": b"state",
     # unique identifier of the chip
     "CLIENT_ID": b"esp8266_" + ubinascii.hexlify(machine.unique_id())
}

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())



# Complete project details at https://RandomNerdTutorials.com


def onMessage(topic, msg):
    print("Topic: %s, Message: %s" % (topic, msg))
 
    if msg == b"on":      
        led.value(1)
    elif msg == b"off":
        led.off()

def listen():
    #Create an instance of MQTTClient 
    client = MQTTClient(CONFIG['CLIENT_ID'], CONFIG['MQTT_BROKER'],port=CONFIG['PORT'])
    # Attach call back handler to be called on receiving messages
    client.set_callback(onMessage)
    client.connect()
    client.publish("test", "ESP8266 is Connected")
    client.subscribe(CONFIG['TOPIC'])
    print("ESP8266 is Connected to %s and subscribed to %s topic" % (CONFIG['MQTT_BROKER'], CONFIG['TOPIC']))
    
    try:
    	while True:
    		msg=client.wait_msg()
    		client.check_msg()
    		
    finally:
    	client.disconnect()
 


def restart_and_reconnect():
	print('Failed to connect to MQTT broker. Reconnecting...')
	time.sleep(10)
	machine.reset()

listen()

  


