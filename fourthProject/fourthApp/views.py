from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request,"fourthapp/index.html")   #location of a html file within template

def forms_name(request):
    form = forms.FormName()



    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():

            #code for true
            ##below it prints out the info you gave in forms page.
            print("valid Input")
            print("Name: "+form.cleaned_data["name"])           ##write the user name in the console.
            print("Email: " + form.cleaned_data["email"])       ##write the user email in the console.
            print("Text: " + form.cleaned_data["text"])         ##write the user comment in the console.

    return render(request, "fourthapp/forms.html", {"fill_form": form})  # location of a html file within template