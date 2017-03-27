from django import forms


class FilterStatusForm(forms.Form):
	CHOICES = (('All', 'All'),('27', '27',), ('71', '71',),('75', '75',), 
		('76', '76',),('81', '81',), ('84', '84',),
		('86', '86',),)
	status = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())