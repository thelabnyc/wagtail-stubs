from django import forms

class EmbedForm(forms.Form):
    url: forms.CharField
