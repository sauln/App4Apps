from app import app, render_template
import markovGen as mg

@app.route('/')
def home():
    return 'hello world'
	
	
	
@app.route('/gen')
def genNew():
	generated_text = mg.generate()


	return render_template("generator.html", generated_text=generated_text)

