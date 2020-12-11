from flask import Flask
import paho.mqtt.client as mqtt
import flask
from flask import request, render_template, make_response
import json
import os


# global state

# state=" " 
topic = 'state'


def onconnect(client, userdata, rc):
    # global state
    state=str(read())
    client.publish(topic, state)
    # client.publish(topic2, "CONNECTED")


def on_message(client, userdata, msg):
    client.publish(topic2, "MESSAGE")
app = flask.Flask(__name__)
app.config["DEBUG"] = True	

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/led')
def led():

    state = request.args.get('state')
    s=str(state)
    client.publish(topic, state) 
    return ('', 204)

	# if 'state' in request.args:
	# 	state = request.args['state']
    # else :
    #     state= "Error"
    
    # client.publish(topic, state) 
    



	# 	s={
	# 	"state":state
	# 	}
	# fname=os.path.join(app.static_folder,"sample.json")
	
	# with open(fname,"w") as outfile:
	# 	json.dump(s,outfile)
	


def read():
	fname=os.path.join(app.static_folder,"sample.json")
	with open(fname,'r') as inputfile:
	
		json_obj=json.load(inputfile)
	
	return json_obj["state"]	



# if __name__ == '__main__':
client = mqtt.Client("server")
    #client.username_pw_set(username, password)
# client.on_connect = onconnect
    #client.on_message = on_message
client.connect('192.168.43.126',port=1883)
    # client.publish(topic, state) 
client.loop_start()

app.run(host='0.0.0.0', port=5000)