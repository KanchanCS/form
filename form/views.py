from django.shortcuts import redirect, render

from .forms import BankRegistrationForm
from .models import BankRegistration

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = BankRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form:register')
    else:
        form = BankRegistrationForm()

    return render(request, "form.html", {'form': form})
