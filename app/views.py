from app import app, render_template
import markov.transition_builder as tran
import markov.chain_builder as chain
from flask.ext.wtf import Form
from wtforms import RadioField

class SimpleForm(Form):
    example = RadioField('Label', choices=[('business','Business'),('communication','Communication'), ('education', 'Education'), ('entertainment', 'Entertainment')])

@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])	
@app.route('/gen', methods=['GET', 'POST'])
def generator():
    form = SimpleForm()
    generated_text=''
    prev = ''
    if form.validate_on_submit():
        print form.example.data
        if form.example.data != prev:
            firstOrder, secondOrder, first = tran.go(form.example.data)
            prev = form.example.data
        generated_text = chain.buildChain(firstOrder, secondOrder, first)
    else:
        print form.errors
    return render_template("generator.html", generated_text=generated_text, form=form)

