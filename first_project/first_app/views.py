from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
from first_app.forms import FormName
from . import forms
# from first_app.models import User
from first_app.forms import NewUserForm
from first_app.models import User

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request,'index.html',context=date_dict)

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Validation Success!")
            print("NAME "+form.cleaned_data['name'])
            print("EMAIL : "+form.cleaned_data['email'])
    return render(request, 'basicapp/form_page.html', {'form':form})

def users(request):
        userform = NewUserForm()
        if request.method == "POST":
                userform = NewUserForm(request.POST)

                if userform.is_valid():
                        userform.save(commit=True)
                        return index(request)
                else:
                        print("ERROR FORM INVALID!")
        return render(request,'users.html', {'form':userform})
        

                

