from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(label='Your Email')
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

