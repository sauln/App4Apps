from app import app, render_template
import markov.transition_builder as tran
import markov.chain_builder as chain





@app.route('/')
def home():
    return 'hello world'
	
	
	
@app.route('/gen')
def genNew():
	

	generated_text = chain.buildChain(
		tran.firstOrder, tran.secondOrder, tran.first)

	return render_template("generator.html", generated_text=generated_text)

