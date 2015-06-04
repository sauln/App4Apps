from app import app, render_template

@app.route('/')
def home():
    return 'hello world'
	
	
	
@app.route('/gen')
def genNew():
	generated_text = "a whole bunch of words"


	render_template("generator.html", generated_text)

