import flask
from flask import request, render_template, make_response
import json
import os


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def index():
	return render_template('index.html')
	
	
	
@app.route('/led')
def led():
	if 'state' in request.args:
		state=str(request.args['state'])
		s={
		"state":state
		}
	fname=os.path.join(app.static_folder,"sample.json")
	
	with open(fname,"w") as outfile:
		json.dump(s,outfile)
	
	return ('', 204)



		
@app.route('/read')
def read():
	fname=os.path.join(app.static_folder,"sample.json")
	with open(fname,'r') as inputfile:
	
		json_obj=json.load(inputfile)
	
	return json_obj["state"]	
	

	
app.run(host="0.0.0.0",port=5000)
    
