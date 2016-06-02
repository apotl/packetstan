from app import app
from flask import render_template, send_file, url_for
from random import randrange
from json import dumps

@app.route('/')
def index():
	#load json line below
	pcap_json_obj = [ [x,randrange(1,10)] for x in range(100)]

	pcap_json_obj.sort(key=lambda pair: pair[0])
	pcap_json_obj = dumps([{'x':pair[0],'y':pair[1]} for pair in pcap_json_obj])

	return render_template("chart.html",
				pcap_json_obj = pcap_json_obj,
	)

@app.route('/includes/<path:include_path>')
def includes(include_path):
	return send_file( '/'.join(__file__.split('/')[:-1]+['static','includes','']) + include_path)
