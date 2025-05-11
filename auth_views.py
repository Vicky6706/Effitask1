from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import FormView, View
from django.shortcuts import render, redirect
from django.contrib.auth import login

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('task-list')

class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect('task-list')
