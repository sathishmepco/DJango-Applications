from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter username','style':'margin:10px 0px 0px 0px'}),required=False)
    password = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password','style':'margin:10px 0px 10px 0px'}),required=False)
    captcha = CaptchaField()
