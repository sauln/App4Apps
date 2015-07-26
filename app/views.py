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
    generated_text=''
    if form.validate_on_submit():
        print form.example.data
        firstOrder, secondOrder, first = tran.go(form.example.data)
        generated_text = chain.buildChain(firstOrder, secondOrder, first)
    else:
        print form.errors
    return render_template("generator.html", generated_text=generated_text, form=form)

