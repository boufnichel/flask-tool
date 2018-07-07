from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route("/<usertext>")
def index(usertext):
	
	apiurl  = "http://sentiment.vivekn.com/api/text/"
	headers = {"Content-Type": "application/x-www-form-urlencoded"}
	payload = {"txt": usertext}

	response = requests.post(apiurl, headers=headers, data=payload)
	

	return render_template('feeling.html', feeling=response.json()['result']['sentiment']);
