from flask import Flask, render_template, request

app = Flask(__name__)

# both GET and POST are used in order to server the index
# page and handle form submissions.
@app.route("/", methods=['GET', 'POST'])
def index():
	errors = []
	results = {}
	if request.method == "POST":
		try:
			diary = request.form['diary']
			
		except:
			errors.append(
				"Unable to read text."
				)
		# get the text that the user entered
	return render_template('index.html', errors=errors, results=results)
