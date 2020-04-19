from flask import Flask,request, render_template
from flask import jsonify


app = Flask(__name__)

@app.route('/',methods=['GET' , 'POST'])
def index():
	print("Hello world")
	msg = "Hello World"
	ob = {
		'id': 1,
		'name': "Vishal"
	}
	return jsonify(ob)
	
if __name__ == "__main__":
  app.run(threaded=False)