from flask import Flask 
app = Flask(__name__)

@app.route('/')

def hello_world():
	return 'Example Flask Server Page! Tabula Rasa'
app.run(debug=True)
