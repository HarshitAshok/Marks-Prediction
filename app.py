from flask import Flask, render_template, redirect, request
import joblib

# __name__  == __main__
app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route('/')
def hello():
	return render_template("index1.html")

@app.route('/', methods=['POST'])
def marks():
	if request.method == 'POST':
		hours = float(request.form['hours'])

		marks = str(round(model.predict([[hours]])[0][0], 2))

	return render_template('index1.html', your_marks = marks)	

if __name__ == '__main__':
	app.run(debug=True)