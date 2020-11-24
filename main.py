from machine import Pin
import urequests
import time
#try:
#  import usocket as socket
#except:
 # import socket


import network



ssid = 'lg'
password = '12345678'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led= Pin(14,Pin.OUT)

while(True):
	try:
		resp=urequests.get("http://192.168.43.126:5000/read")
		if resp.text== "on":
			led.value(1)
			time.sleep(2)
		else:
			led.value(0)
			time.sleep(2)
	except:
		pass
		
		
		
