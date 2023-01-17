from django import forms

class CantactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
    person = forms.IntegerField()