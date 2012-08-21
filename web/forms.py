from django import forms
from captcha.fields import ReCaptchaField


class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField()
	captcha = ReCaptchaField()
