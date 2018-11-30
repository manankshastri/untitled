from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'check/index.html')


def register(request):
    form = UserCreationForm()
    context = {'form' : form}
    render(request, 'registration/register.html', context)

