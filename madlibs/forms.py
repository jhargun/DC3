from django import forms

#Dragon
class form1(forms.Form):
    a = forms.CharField(label='Color', max_length=100)
    b = forms.CharField(label='Superlative ending with -est', max_length=100)
    c = forms.CharField(label='Adjective', max_length=100)
    d = forms.CharField(label='Body part (plural)', max_length=100)
    e = forms.CharField(label='Body part', max_length=100)
    f = forms.CharField(label='Noun', max_length=100)
    g = forms.CharField(label='Animal (plural)', max_length=100)
    h = forms.CharField(label='Adjective', max_length=100)
    i = forms.CharField(label='Adjective', max_length=100)
    j = forms.CharField(label='Adjective', max_length=100)

class form2 (forms.Form):
    a = forms.CharField(label='Silly word', max_length=100)
    b = forms.CharField(label='Last name', max_length=100)
    c = forms.CharField(label='Illness', max_length=100)
    d = forms.CharField(label='Noun (plural)', max_length=100)
    e = forms.CharField(label='Adjective', max_length=100)
    f = forms.CharField(label='Adjective', max_length=100)
    g = forms.CharField(label='Silly word', max_length=100)
    h = forms.CharField(label='Place', max_length=100)
    i = forms.CharField(label='Number', max_length=100)
    j = forms.CharField(label='Adjective', max_length=100)