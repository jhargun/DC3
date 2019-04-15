from django import forms

class form1(forms.Form):
    one = forms.CharField(label='Color', max_length=100)