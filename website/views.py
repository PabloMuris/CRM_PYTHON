from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignupForm
from .models import Record

def home(request):

    records = Record.objects.all()
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username= username,password = password)
        if user is not None:
            login(request,user)
            messages.success(request, "voce logou")
            return redirect('home')
        else:
            messages.success(request,'Algo errado aconteceu durante o login. Tente de novo ')
            return redirect('home')
    else:
        return render(request,'home.html',{})
    
def logout_user(request):
    logout(request)
    messages.success(request, ' você fez logout')
    return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Você entrou. Bem-vindo")
			return redirect('home')
	else:
		form = SignupForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})
 