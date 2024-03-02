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

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'Usuário'
            self.fields['username'].label = ''
            self.fields['username'].help_text = '<span class="form-text text-muted"><small>Necessário 150 characters ou menos. Letras, digitos e @/./+/-/_ only.</small></span>'

            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
            self.fields['password1'].label = ''
            self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Sua senha não deve conter informações pessoais.</li><li>Sua senha deve ter no minimo 8 digitos</li><li>Evite senhas muito comuns</li><li>Senhas que tenham apenas número snão serão aceitas.</li></ul>'

            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirme a senha'
            self.fields['password2'].label = ''
            self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Digite o mesmo email, para verifficação</small></span>'	

