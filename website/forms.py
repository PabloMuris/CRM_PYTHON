from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class SignupForm(UserCreationForm):
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    first_name = forms.CharField(label='',max_length=120,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nome'}))
    last_name = forms.CharField(label='',max_length=120,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Sobrenome'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

        def __init__(self,*args,**kwargs):
            super(SignupForm,self).__init__(*args,**kwargs)
