from app import app, render_template
import markov.transition_builder as tran
import markov.chain_builder as chain





@app.route('/')	
def home():
	return render_template("home_page.html")




@app.route('/gen')
def generator():
	
	generated_text = chain.buildChain(
		tran.firstOrder, tran.secondOrder, tran.first)

	return render_template("generator.html", generated_text=generated_text)

