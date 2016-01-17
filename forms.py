from django import forms

class OptionsRadio(forms.Form):
	CHOICES=[('business', 'Business'),
			 ('finance', 'Finance'),
			 ('education', 'Education')]
	option = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())



