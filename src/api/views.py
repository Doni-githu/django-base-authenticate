from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationForm2
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login


class Register(View):
    template_name = "registration/register.html"
    
    def get(self, request):
        context = {
            'form':  UserCreationForm2()
        }
        return render(request,self.template_name, context)
    
    def post(self, request):
        form = UserCreationForm2(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        
        return render(request, self.template_name, context)
            