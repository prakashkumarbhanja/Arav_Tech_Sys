from django.shortcuts import render
from django.http import HttpResponse
from employee.forms import UserForm
# Create your views here.
def test(request):
    template = 'poll/index.html'
    return render(request, template)

def employe_add(request):#25

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponse('Employee Added Successfully')
        else:
            return render(request, 'employee/add.html', {"user_form": user_form})
    else:
        user_form = UserForm()
        return render(request, 'employee/add.html', {"user_form": user_form})
