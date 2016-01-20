from django.shortcuts import render
from app4apps.forms import OptionsRadio
from app4apps.services import new_text





def app_page(request):
	if request.method == 'POST':
		form = OptionsRadio(request.POST)
		if form.is_valid():
			value = form.cleaned_data['option']
			text = new_text(value)
		return render(request, 'app4app.html', {
		  		'fauxText':text, 
				'form':form, 
				'category':value
				})
	else:
		form = OptionsRadio()


	return render(request, 'app4app.html', {
	  		'form':form, 
			'category':'business'
			})

