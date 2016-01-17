from django.shortcuts import render
from app4apps.forms import OptionsRadio


def app_page(request):
	if request.method == 'POST':
		form = OptionsRadio(request.POST)
		if form.is_valid():
			print(form)
			value = form.cleaned_data['option']
		return render(request, 'app4app.html', {'fauxText': "you selected %s"%value, 'form':form, 'category':value})
	else:
		form = OptionsRadio()

	print(form)
	return render(request, 'app4app.html', {'fauxText': "Hi How's it going", 'form':form, 'category':'business'})

