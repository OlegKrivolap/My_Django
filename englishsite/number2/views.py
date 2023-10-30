from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import RegistrationForm


def get_all_users(request):
    pass



def get_user(request):
    pass
def add_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return render(request, 'success.html')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistrationForm()

    return render(request, "registration.html", {"form": form})

