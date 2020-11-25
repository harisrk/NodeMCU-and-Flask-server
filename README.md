# NodeMCU and Flask Server

This  is an simple project for blinking an LED using the ESP8266 NodeMCU from an Server.

The project use FLask as  the server and Micropython for NodeMCU

# Setup

 - Install Pipenv
 - pipenv shell
 - pipenv install 
 
 
## Server
 
 	To run server 'python server.py' 
 	
## NodeMCU 
 	
 	Download from [micropython firmware](https://micropython.org/download/esp8266/)
 	
 	Upload the firmware using esptool
 		'esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin'
 	upload the code to nodemcu using the adafruit
 		'ampy --port /dev/ttyUSB0 -b 115200  put main.py'
 		
 		
 	
 Note: Here I connected the  nodemcu  and the server to a common network;

 	
 	
 

