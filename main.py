from flask import Flask,request, render_template

app = Flask(__name__)

@app.route('/',methods=['GET' , 'POST'])
def index():
	print("Hello world")
	msg = "Hello World"
	return render_template('index.html', message = msg)
	
if __name__ == "__main__":
  app.run(threaded=False)