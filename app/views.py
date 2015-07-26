from app import app, render_template
import markov.transition_builder as tran
import markov.chain_builder as chain
from flask.ext.wtf import Form
from wtforms import RadioField

class SimpleForm(Form):
    example = RadioField('Label', choices=[('business','Business'),('communication','Communication'), ('education', 'Education'), ('entertainment', 'Entertainment')])

@app.route('/index')
@app.route('/', methods=['GET', 'POST'])	
@app.route('/gen')
def generator():
    form = SimpleForm()
    if form.validate_on_submit():
        print form.example.data
    else:
        print form.errors
    generated_text = chain.buildChain(tran.firstOrder, tran.secondOrder, tran.first)
    return render_template("generator.html", generated_text=generated_text, form=form)

