from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth import login, authenticate
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import UserCreationForm



class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks:main')



class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy('tasks:main')
    form_class = UserCreationForm
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        new_user = form.save()
        if new_user is not None:
            new_user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(self.request, new_user)
        return HttpResponseRedirect(reverse('tasks:main'))

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks:main')
        return super(SignUpView, self).get(*args, **kwargs)