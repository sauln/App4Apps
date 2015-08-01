from app import app, render_template


#import markov.transition_builder as tran
#import markov.chain_builder as chain

import markov.markov_chain as markov

mc = dict()

categories = [ "business", "education", "finance", "test"]

for each in categories:
	mc[each] = markov.load_dictionary(each)








#g = mc.buildChain(50)




from flask.ext.wtf import Form
from wtforms import RadioField


class SimpleForm(Form):
    example = RadioField('Label', choices=[('business','Business '),
											('test', 'Test'),
                                           #('communication','Communication '), 
                                           ('education', 'Education '), 
                                           #('entertainment', 'Entertainment '), 
                                           ('finance', 'Finance '), 
                                           #('medical', 'Medical '), 
                                           #('photography', 'Photography '), 
                                           #('social', 'Social '), 
                                           #('sports', 'Sports ')
										   ])

										   
										   
@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])	
@app.route('/gen', methods=['GET', 'POST'])


def generator():
    form = SimpleForm()
    generated_text=''
    prev = ''
    done=False
    if form.validate_on_submit():
		print form.example.data
		generated_text = mc[form.example.data].buildChain(50)
    else:
        print form.errors
		
		
    return render_template("generator.html", generated_text=generated_text, form=form)

