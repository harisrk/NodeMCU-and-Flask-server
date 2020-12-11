from flask import Flask
from flask_mqtt import Mqtt


app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = '192.168.43.126'  # use the free broker from HIVEMQ
app.config['MQTT_BROKER_PORT'] = 1883  # default port for non-tls connection
app.config['MQTT_USERNAME'] = ''  # set the username here if you need authentication for the broker
app.config['MQTT_PASSWORD'] = ''  # set the password here if the broker demands authentication
app.config['MQTT_KEEPALIVE'] = 5  # set the time interval for sending a ping to the broker to 5 seconds
app.config['MQTT_TLS_ENABLED'] = False  # set TLS to disabled for testing purposes

mqtt = Mqtt(app)
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/led')
def led():

    state = request.args.get('state')
    s=str(state)
    mqtt.publish('state', state)    
    return ('', 204)